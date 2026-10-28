import csv
import io
import json
import os
import quopri
import re
import threading
import unicodedata
from datetime import datetime, timezone, timedelta  # <-- AÑADIDO: timedelta
from uuid import uuid4

import requests                                     # <-- NUEVO
from dotenv import load_dotenv                      # <-- NUEVO
from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    send_file,
)

load_dotenv()  # <-- NUEVO: Carga las variables del archivo .env al iniciar

app = Flask(__name__)

# Límite general para las solicitudes que incluyen archivos o imágenes.
app.config["MAX_CONTENT_LENGTH"] = int(os.getenv("MAX_CONTENT_LENGTH", 12 * 1024 * 1024))

# Archivos y carpetas ubicados junto a app.py.
BASE = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE, "contactos.json")
PLANTILLAS_DIR = os.path.join(BASE, "plantillas")

# Solo se permiten identificadores hexadecimales de 32 caracteres.
ID_RE = re.compile(r"^[0-9a-f]{32}$")
LINK_RE = re.compile(r"^https?://\S+$", re.IGNORECASE)

# Código de país que se antepone a los números locales al IMPORTAR.
# <-- MODIFICADO: Ahora se lee del .env, con "56" como fallback
# Código de país que se antepone a los números locales al IMPORTAR
PAIS_DEFECTO = "56"
# -------------------------------------------------------------------
# CARGA DE PAÍSES DESDE JSON LOCAL
# -------------------------------------------------------------------
ARCHIVO_PAISES = os.path.join(BASE, "paises.json")


def iso_a_bandera(codigo_iso):
    """
    Convierte un código ISO de 2 letras (ej: 'CL') en emoji de bandera (🇨🇱).
    Funciona usando los caracteres Unicode de indicadores regionales.
    """
    if not codigo_iso or len(codigo_iso) != 2:
        return "🏳️"
    return "".join(chr(ord(c.upper()) + 127397) for c in codigo_iso)


def cargar_lista_paises():
    """
    Carga paises.json y lo transforma al formato que espera el frontend:
    {"nombre": "...", "codigo": "...", "flag": "...", "cca2": "..."}
    """
    try:
        with open(ARCHIVO_PAISES, "r", encoding="utf-8") as archivo:
            datos_crudos = json.load(archivo)
        
        # Transformar cada país al formato esperado
        paises = []
        for item in datos_crudos:
            if not isinstance(item, dict):
                continue
            
            pais = {
                "nombre": item.get("country", ""),
                "codigo": item.get("code", ""),
                "flag": iso_a_bandera(item.get("iso", "")),
                "cca2": item.get("iso", "")
            }
            
            # Solo incluir si tiene nombre y código
            if pais["nombre"] and pais["codigo"]:
                paises.append(pais)
        
        # Ordenar alfabéticamente por nombre
        return sorted(paises, key=lambda x: x["nombre"])
    
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error cargando paises.json: {e}")
        # Fallback mínimo para que la app nunca se rompa
        return [{"nombre": "Chile", "codigo": "56", "flag": "🇨🇱", "cca2": "CL"}]


# Cargar una sola vez al iniciar la aplicación
PAISES_DISPONIBLES = cargar_lista_paises()
LIMITE_IMPORTACION = int(os.getenv("LIMITE_IMPORTACION", 10 * 1024 * 1024))
MAX_ERRORES_MOSTRADOS = 50

# Evita que dos peticiones simultáneas pisen contactos.json.
BLOQUEO = threading.RLock()

# <-- NUEVO: Caché en memoria para la API de países
countries_cache = {
    'data': None,
    'timestamp': None
}

@app.errorhandler(413)
def archivo_muy_grande(_error):
    return jsonify(error="El archivo supera el límite de 12 MB."), 413


# -------------------------------------------------------------------
# UTILIDADES JSON
# -------------------------------------------------------------------

def escribir_json(ruta, datos):
    """Guarda JSON usando un archivo temporal para reducir riesgos."""
    tmp = ruta + ".tmp"

    with open(tmp, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)

    os.replace(tmp, ruta)


def cargar_contactos():
    """Carga los contactos y actualiza registros antiguos."""
    with BLOQUEO:
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                contactos = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

        if not isinstance(contactos, list):
            return []

        modificados = False

        for contacto in contactos:
            if not isinstance(contacto, dict):
                continue

            if not contacto.get("id"):
                contacto["id"] = uuid4().hex
                modificados = True

            if "link" not in contacto:
                contacto["link"] = ""
                modificados = True

        if modificados:
            guardar_contactos(contactos)

        return [c for c in contactos if isinstance(c, dict)]


def guardar_contactos(contactos):
    """Guarda la lista de contactos."""
    escribir_json(ARCHIVO, contactos)


def ruta_plantilla(pid):
    """Devuelve la ruta de una plantilla si el identificador es válido."""
    if not isinstance(pid, str) or not ID_RE.fullmatch(pid):
        return None

    return os.path.join(PLANTILLAS_DIR, pid + ".json")


def leer_plantilla(pid):
    """Lee una plantilla por su identificador."""
    ruta = ruta_plantilla(pid)

    if not ruta:
        return None

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


# -------------------------------------------------------------------
# VALIDACIÓN COMÚN DE CONTACTOS
# -------------------------------------------------------------------

def solo_digitos(valor):
    return "".join(c for c in str(valor or "") if c.isdigit())


def normalizar_telefono(crudo):
    """
    Limpia un teléfono importado:
    +56 9 1234 5678 -> 56912345678
    0056912345678   -> 56912345678
    912345678       -> 56912345678 (si PAIS_DEFECTO está definido)
    """
    texto = str(crudo or "").strip()
    digitos = solo_digitos(texto)

    if texto.startswith("+"):
        return digitos

    if digitos.startswith("00"):
        return digitos[2:]

    if PAIS_DEFECTO and len(digitos) == 9 and digitos.startswith("9"):
        return PAIS_DEFECTO + digitos

    return digitos


def telefono_valido(telefono):
    return 8 <= len(telefono) <= 15


def validar_contacto(nombre, telefono, link, importando=False):
    """
    Devuelve (contacto, None) o (None, motivo).
    Al importar, se normaliza el teléfono con el código de país por
    defecto; al guardar a mano solo se conservan los dígitos.
    """
    nombre = str(nombre or "").strip()[:120]
    link = str(link or "").strip()
    telefono = (
        normalizar_telefono(telefono)
        if importando
        else solo_digitos(telefono)
    )

    if not nombre:
        return None, "El nombre es obligatorio."

    if not telefono_valido(telefono):
        return None, (
            "El teléfono debe tener entre 8 y 15 dígitos, "
            "incluyendo el código de país."
        )

    if link and not LINK_RE.match(link):
        return None, "El link debe empezar con http:// o https://"

    return {"nombre": nombre, "telefono": telefono, "link": link}, None


# -------------------------------------------------------------------
# UTILIDADES VCARD / VCF
# -------------------------------------------------------------------

def escapar_vcard(valor):
    """Escapa caracteres especiales de los campos de texto vCard."""
    return (
        str(valor)
        .replace("\\", "\\\\")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("\n", "\\n")
        .replace(",", "\\,")
        .replace(";", "\\;")
    )


def desescapar_vcard(valor):
    """Revierte los escapes habituales de vCard."""
    resultado = []
    i = 0

    while i < len(valor):
        if valor[i] == "\\" and i + 1 < len(valor):
            siguiente = valor[i + 1]

            if siguiente in ("n", "N"):
                resultado.append("\n")
            elif siguiente in (",", ";", "\\"):
                resultado.append(siguiente)
            else:
                resultado.extend(("\\", siguiente))

            i += 2
        else:
            resultado.append(valor[i])
            i += 1

    return "".join(resultado)


def plegar_linea(linea, limite=75):
    """Pliega líneas largas a 75 bytes sin cortar caracteres UTF-8."""
    salida = []
    actual = ""
    tamano = 0

    for caracter in linea:
        peso = len(caracter.encode("utf-8"))

        if tamano + peso > limite:
            salida.append(actual)
            actual = " " + caracter
            tamano = 1 + peso
        else:
            actual += caracter
            tamano += peso

    salida.append(actual)
    return "\r\n".join(salida)


def decodificar_texto(contenido):
    """Decodifica bytes como UTF-8 y, si falla, como Windows-1252."""
    try:
        return contenido.decode("utf-8-sig")
    except UnicodeDecodeError:
        return contenido.decode("cp1252", errors="replace")


def desplegar_lineas(texto):
    """
    Une las líneas continuadas de un VCF:
    - las que empiezan con espacio o tabulación (vCard 3.0 y 4.0)
    - las de QUOTED-PRINTABLE que terminan en "=" (vCard 2.1)
    """
    unidas = []
    continuar_qp = False

    for linea in texto.split("\n"):
        if continuar_qp and unidas:
            unidas[-1] = unidas[-1][:-1] + linea
        elif linea.startswith((" ", "\t")) and unidas:
            unidas[-1] += linea[1:]
        else:
            unidas.append(linea)

        ultima = unidas[-1]
        continuar_qp = (
            "QUOTED-PRINTABLE" in ultima.upper()
            and ultima.endswith("=")
        )

    return unidas


def decodificar_valor_vcard(valor, parametros):
    """Decodifica valores QUOTED-PRINTABLE (frecuentes en vCard 2.1)."""
    if not any("QUOTED-PRINTABLE" in p for p in parametros):
        return valor

    charset = "utf-8"

    for parametro in parametros:
        if parametro.startswith("CHARSET="):
            charset = parametro.split("=", 1)[1].strip().lower()

    try:
        crudo = quopri.decodestring(valor.encode("ascii", "ignore"))
        return crudo.decode(charset, errors="replace")
    except (LookupError, ValueError):
        return valor


def nombre_desde_n(valor_n):
    """Reconstruye el nombre desde N: apellido;nombre;segundo;prefijo;sufijo."""
    partes = valor_n.split(";")
    partes += [""] * (5 - len(partes))
    apellido, nombre_pila, segundo, prefijo, sufijo = partes[:5]

    return " ".join(
        p.strip()
        for p in (prefijo, nombre_pila, segundo, apellido, sufijo)
        if p.strip()
    )


def leer_vcf(contenido):
    """
    Convierte un VCF en contactos. Admite vCard 2.1, 3.0 y 4.0.
    Devuelve (registros, invalidos).
    """
    texto = decodificar_texto(contenido)
    texto = texto.replace("\r\n", "\n").replace("\r", "\n")

    registros = []
    invalidos = []
    actual = None
    numero = 0

    for linea in desplegar_lineas(texto):
        limpia = linea.strip()

        if limpia.upper() == "BEGIN:VCARD":
            actual = {"telefonos": []}
            numero += 1
            continue

        if limpia.upper() == "END:VCARD":
            if actual is not None:
                cerrar_tarjeta(actual, numero, registros, invalidos)
            actual = None
            continue

        if actual is None or ":" not in linea:
            continue

        propiedad, valor = linea.split(":", 1)
        partes = propiedad.split(";")
        campo = partes[0].split(".")[-1].upper()
        parametros = [p.upper() for p in partes[1:]]

        # Se ignoran fotos, claves y demás campos pesados.
        if campo not in ("FN", "N", "TEL", "URL"):
            continue

        valor = decodificar_valor_vcard(valor, parametros).strip()

        if campo == "FN" and "FN" not in actual:
            actual["FN"] = valor
        elif campo == "N" and "N" not in actual:
            actual["N"] = valor
        elif campo == "URL" and "URL" not in actual:
            actual["URL"] = valor
        elif campo == "TEL":
            actual["telefonos"].append((valor, parametros))

    return registros, invalidos


def cerrar_tarjeta(tarjeta, numero, registros, invalidos):
    nombre = tarjeta.get("FN", "").strip()

    if not nombre and tarjeta.get("N"):
        nombre = nombre_desde_n(tarjeta["N"])

    # Prefiere los números marcados como celular.
    telefonos = sorted(
        tarjeta["telefonos"],
        key=lambda t: 0 if any("CELL" in p for p in t[1]) else 1,
    )

    construir_registro(
        desescapar_vcard(nombre),
        elegir_telefono([t[0] for t in telefonos]),
        desescapar_vcard(tarjeta.get("URL", "")),
        f"Contacto {numero}",
        registros,
        invalidos,
    )


# -------------------------------------------------------------------
# LECTORES CSV / JSON
# -------------------------------------------------------------------

def normalizar_columna(texto):
    sin_acentos = unicodedata.normalize("NFKD", str(texto))
    sin_acentos = "".join(
        c for c in sin_acentos if not unicodedata.combining(c)
    )
    return re.sub(r"\s+", " ", sin_acentos).strip().lower()


ALIAS_NOMBRE = {
    "nombre", "name", "nombre completo", "full name", "contacto",
    "display name", "fn",
}
ALIAS_PILA = {"first name", "given name", "nombres", "nombre de pila"}
ALIAS_APELLIDO = {"last name", "family name", "apellido", "apellidos"}
ALIAS_TELEFONO = {
    "telefono", "tel", "phone", "celular", "movil", "mobile",
    "whatsapp", "numero", "numero de telefono", "phone number",
}
ALIAS_LINK = {
    "link", "url", "sitio web", "web", "website", "pagina",
    "pagina web", "enlace",
}


def indice(cabecera, alias):
    for i, columna in enumerate(cabecera):
        if columna in alias:
            return i
    return None


def elegir_telefono(candidatos):
    """Devuelve el primer teléfono válido; si no hay, el primero."""
    candidatos = [c for c in candidatos if str(c).strip()]

    for candidato in candidatos:
        if telefono_valido(normalizar_telefono(candidato)):
            return candidato

    return candidatos[0] if candidatos else ""


def construir_registro(nombre, telefono, link, referencia,
                       registros, invalidos):
    """Valida un contacto importado y lo agrega a la lista correcta."""
    link = str(link or "").strip()

    # Un link inválido no descarta el contacto: simplemente se omite.
    if not LINK_RE.match(link):
        link = ""

    registro, motivo = validar_contacto(
        nombre, telefono, link, importando=True
    )

    if registro:
        registros.append(registro)
    else:
        invalidos.append({
            "referencia": referencia,
            "nombre": str(nombre or "").strip()[:120],
            "motivo": motivo,
        })


def limpiar_celda(valor):
    """Quita el apóstrofo que se agrega al exportar para evitar fórmulas."""
    valor = str(valor or "").strip()

    if len(valor) > 1 and valor[0] == "'" and valor[1] in "=+-@":
        return valor[1:]

    return valor


def leer_csv(contenido):
    texto = decodificar_texto(contenido)

    if not texto.strip():
        raise ValueError("El archivo CSV está vacío.")

    primera = texto.strip().splitlines()[0]
    separador = max((";", ",", "\t"), key=primera.count)

    filas = list(csv.reader(io.StringIO(texto), delimiter=separador))
    cabecera = [normalizar_columna(c) for c in filas[0]]

    col_nombre = indice(cabecera, ALIAS_NOMBRE)
    col_pila = indice(cabecera, ALIAS_PILA)
    col_apellido = indice(cabecera, ALIAS_APELLIDO)
    col_link = indice(cabecera, ALIAS_LINK)

    # Incluye columnas tipo "Phone 1 - Value" de Google Contacts.
    cols_tel = [
        i for i, c in enumerate(cabecera)
        if c in ALIAS_TELEFONO or re.match(r"^phone \d+ - value$", c)
    ]

    if not cols_tel or (
        col_nombre is None and col_pila is None
    ):
        raise ValueError(
            "No se encontraron las columnas de nombre y teléfono. "
            "Usa los encabezados: nombre, telefono, link."
        )

    def celda(fila, i):
        return limpiar_celda(fila[i]) if i is not None and i < len(fila) else ""

    registros = []
    invalidos = []

    for numero, fila in enumerate(filas[1:], start=2):
        if not any(c.strip() for c in fila):
            continue

        if col_nombre is not None:
            nombre = celda(fila, col_nombre)
        else:
            nombre = " ".join(
                p for p in (celda(fila, col_pila), celda(fila, col_apellido))
                if p
            )

        candidatos = []

        for i in cols_tel:
            # Google separa varios números de una celda con " ::: ".
            candidatos.extend(celda(fila, i).split(":::"))

        construir_registro(
            nombre,
            elegir_telefono(candidatos),
            celda(fila, col_link),
            f"Fila {numero}",
            registros,
            invalidos,
        )

    return registros, invalidos


def leer_json(contenido):
    try:
        datos = json.loads(decodificar_texto(contenido))
    except json.JSONDecodeError:
        raise ValueError("El archivo JSON no es válido.")

    if isinstance(datos, dict):
        datos = datos.get("contactos", [])

    if not isinstance(datos, list):
        raise ValueError("El JSON debe contener una lista de contactos.")

    registros = []
    invalidos = []

    for numero, item in enumerate(datos, start=1):
        if not isinstance(item, dict):
            invalidos.append({
                "referencia": f"Elemento {numero}",
                "nombre": "",
                "motivo": "No es un contacto válido.",
            })
            continue

        construir_registro(
            item.get("nombre") or item.get("name"),
            item.get("telefono") or item.get("phone"),
            item.get("link") or item.get("url"),
            f"Elemento {numero}",
            registros,
            invalidos,
        )

    return registros, invalidos


LECTORES = {".vcf": leer_vcf, ".csv": leer_csv, ".json": leer_json}


# -------------------------------------------------------------------
# PÁGINAS
# -------------------------------------------------------------------

@app.get("/")
def index():
    return render_template("index.html")


@app.get("/editor")
def editor():
    return render_template("editor.html")


@app.get("/p/<pid>")
def ver_plantilla(pid):
    if leer_plantilla(pid) is None:
        return "Plantilla no encontrada.", 404

    return render_template("compartido.html", pid=pid)


# -------------------------------------------------------------------
# API DE CONTACTOS
# -------------------------------------------------------------------

@app.get("/api/contactos")
def listar():
    return jsonify(cargar_contactos())


@app.post("/api/contactos")
def crear():
    datos = request.get_json(silent=True) or {}

    registro, error = validar_contacto(
        datos.get("nombre"), datos.get("telefono"), datos.get("link")
    )

    if error:
        return jsonify(error=error), 400

    with BLOQUEO:
        contactos = cargar_contactos()

        if any(
            str(c.get("telefono", "")) == registro["telefono"]
            for c in contactos
        ):
            return jsonify(error="Ese teléfono ya está en tu lista."), 409

        nuevo = {"id": uuid4().hex, **registro}
        contactos.append(nuevo)
        guardar_contactos(contactos)

    return jsonify(nuevo), 201


@app.put("/api/contactos/<contacto_id>")
def actualizar(contacto_id):
    datos = request.get_json(silent=True) or {}

    registro, error = validar_contacto(
        datos.get("nombre"), datos.get("telefono"), datos.get("link")
    )

    if error:
        return jsonify(error=error), 400

    with BLOQUEO:
        contactos = cargar_contactos()
        objetivo = next(
            (c for c in contactos if c.get("id") == contacto_id), None
        )

        if objetivo is None:
            return jsonify(error="Contacto no encontrado."), 404

        if any(
            c.get("id") != contacto_id
            and str(c.get("telefono", "")) == registro["telefono"]
            for c in contactos
        ):
            return jsonify(
                error="Ese teléfono ya pertenece a otro contacto."
            ), 409

        objetivo.update(registro)
        guardar_contactos(contactos)

    return jsonify(objetivo)


@app.delete("/api/contactos/<contacto_id>")
def eliminar(contacto_id):
    with BLOQUEO:
        contactos = cargar_contactos()
        restantes = [c for c in contactos if c.get("id") != contacto_id]

        if len(restantes) == len(contactos):
            return jsonify(error="Contacto no encontrado."), 404

        guardar_contactos(restantes)

    return jsonify(ok=True)


# -------------------------------------------------------------------
# IMPORTAR CONTACTOS (VCF, CSV o JSON)
# -------------------------------------------------------------------

@app.post("/api/contactos/importar")
def importar():
    """
    Campos del formulario:
      archivo     -> .vcf, .csv o .json
      modo        -> "vista-previa" (no guarda nada) o "importar"
      duplicados  -> "omitir" (por defecto) o "actualizar"
    """
    archivo = request.files.get("archivo")
    modo = request.form.get("modo", "vista-previa")
    actualizar_existentes = request.form.get("duplicados") == "actualizar"

    if not archivo or not archivo.filename:
        return jsonify(error="Selecciona un archivo."), 400

    extension = os.path.splitext(archivo.filename.lower())[1]

    if extension not in LECTORES:
        return jsonify(
            error="Formato no admitido. Usa .vcf, .csv o .json."
        ), 400

    contenido = archivo.read()

    if not contenido:
        return jsonify(error="El archivo está vacío."), 400

    if len(contenido) > LIMITE_IMPORTACION:
        return jsonify(error="El archivo supera el límite de 10 MB."), 413

    try:
        registros, invalidos = LECTORES[extension](contenido)
    except ValueError as error:
        return jsonify(error=str(error)), 400

    if not registros:
        return jsonify(
            error=(
                "No se encontraron contactos válidos. "
                "Comprueba que tengan nombre y teléfono."
            ),
            total_invalidos=len(invalidos),
            invalidos=invalidos[:MAX_ERRORES_MOSTRADOS],
        ), 400

    with BLOQUEO:
        contactos = cargar_contactos()
        por_telefono = {str(c.get("telefono", "")): c for c in contactos}

        vistos = set()
        nuevos = []
        existentes = []
        repetidos = 0

        for registro in registros:
            telefono = registro["telefono"]

            if telefono in vistos:
                repetidos += 1
                continue

            vistos.add(telefono)

            if telefono in por_telefono:
                existentes.append(registro)
            else:
                nuevos.append(registro)

        respuesta = {
            "ok": True,
            "formato": extension[1:],
            "total_leidos": len(registros) + len(invalidos),
            "nuevos": len(nuevos),
            "duplicados": len(existentes),
            "repetidos_en_archivo": repetidos,
            "total_invalidos": len(invalidos),
            "invalidos": invalidos[:MAX_ERRORES_MOSTRADOS],
            "muestra": nuevos[:6],
        }

        if modo != "importar":
            return jsonify(respuesta)

        actualizados = 0

        if actualizar_existentes:
            for registro in existentes:
                actual = por_telefono[registro["telefono"]]
                cambio = False

                if registro["nombre"] != actual.get("nombre"):
                    actual["nombre"] = registro["nombre"]
                    cambio = True

                if registro["link"] and registro["link"] != actual.get("link"):
                    actual["link"] = registro["link"]
                    cambio = True

                actualizados += cambio

        for registro in nuevos:
            contactos.append({"id": uuid4().hex, **registro})

        if nuevos or actualizados:
            guardar_contactos(contactos)

    partes = [f"{len(nuevos)} agregados"]

    if actualizados:
        partes.append(f"{actualizados} actualizados")

    omitidos = len(existentes) - actualizados

    if omitidos:
        partes.append(f"{omitidos} omitidos por duplicado")

    if invalidos:
        partes.append(f"{len(invalidos)} con errores")

    respuesta.update(
        importados=len(nuevos),
        actualizados=actualizados,
        omitidos=omitidos,
        total=len(contactos),
        mensaje="Importación completada: " + ", ".join(partes) + ".",
    )

    return jsonify(respuesta)


# -------------------------------------------------------------------
# EXPORTAR CONTACTOS (VCF, CSV o JSON)
# -------------------------------------------------------------------

def separar_nombre(nombre):
    """Devuelve (apellido, nombres) para la propiedad N de vCard."""
    palabras = nombre.split()

    if len(palabras) > 1:
        return palabras[-1], " ".join(palabras[:-1])

    return "", nombre


def exportar_vcf_texto(contactos):
    lineas = []

    for c in contactos:
        apellido, nombres = separar_nombre(c["nombre"])

        lineas.extend([
            "BEGIN:VCARD",
            "VERSION:3.0",
            f"FN:{escapar_vcard(c['nombre'])}",
            f"N:{escapar_vcard(apellido)};{escapar_vcard(nombres)};;;",
            f"TEL;TYPE=CELL:+{c['telefono']}",
        ])

        if c["link"]:
            lineas.append(f"URL:{c['link']}")

        lineas.append("END:VCARD")

    return "\r\n".join(plegar_linea(l) for l in lineas) + "\r\n"


def proteger_celda(valor):
    """Evita que Excel interprete un texto como fórmula."""
    valor = str(valor)
    return "'" + valor if valor[:1] in ("=", "+", "-", "@") else valor


def exportar_csv_texto(contactos):
    salida = io.StringIO()
    escritor = csv.writer(salida, delimiter=";", lineterminator="\r\n")
    escritor.writerow(["nombre", "telefono", "link"])

    for c in contactos:
        escritor.writerow([
            proteger_celda(c["nombre"]),
            c["telefono"],
            c["link"],
        ])

    return salida.getvalue()


def exportar_json_texto(contactos):
    return json.dumps(
        {
            "version": 1,
            "exportado": datetime.now(timezone.utc).isoformat(),
            "contactos": contactos,
        },
        ensure_ascii=False,
        indent=2,
    )


FORMATOS_EXPORTACION = {
    "vcf": ("text/vcard; charset=utf-8", exportar_vcf_texto, "utf-8"),
    "csv": ("text/csv; charset=utf-8", exportar_csv_texto, "utf-8-sig"),
    "json": ("application/json", exportar_json_texto, "utf-8"),
}


def generar_exportacion(formato):
    formato = (formato or "vcf").lower()

    if formato not in FORMATOS_EXPORTACION:
        return jsonify(error="Formato de exportación no válido."), 400

    contactos = []

    for c in cargar_contactos():
        nombre = str(c.get("nombre", "")).strip()
        telefono = solo_digitos(c.get("telefono", ""))
        link = str(c.get("link", "")).strip()

        if nombre and telefono:
            contactos.append({
                "nombre": nombre,
                "telefono": telefono,
                "link": link if LINK_RE.match(link) else "",
            })

    if not contactos:
        return jsonify(error="No hay contactos para exportar."), 404

    mimetype, construir, codificacion = FORMATOS_EXPORTACION[formato]
    contenido = construir(contactos).encode(codificacion)
    fecha = datetime.now().strftime("%Y-%m-%d")

    respuesta = send_file(
        io.BytesIO(contenido),
        mimetype=mimetype,
        as_attachment=True,
        download_name=f"contactos_caytech_{fecha}.{formato}",
    )
    respuesta.headers["Cache-Control"] = "no-store"
    return respuesta


@app.get("/api/contactos/exportar")
def exportar():
    return generar_exportacion(request.args.get("formato", "vcf"))


@app.get("/api/contactos/exportar-vcf")
def exportar_vcf():
    """Ruta anterior; se mantiene por compatibilidad."""
    return generar_exportacion("vcf")


@app.get("/api/contactos/ejemplo.csv")
def ejemplo_csv():
    ejemplo = exportar_csv_texto([
        {
            "nombre": "María Pérez",
            "telefono": "56912345678",
            "link": "https://tusitio.cl",
        },
        {
            "nombre": "Juan Soto",
            "telefono": "56987654321",
            "link": "",
        },
    ])

    return send_file(
        io.BytesIO(ejemplo.encode("utf-8-sig")),
        mimetype="text/csv; charset=utf-8",
        as_attachment=True,
        download_name="ejemplo_contactos.csv",
    )


# -------------------------------------------------------------------
# API DE PLANTILLAS
# -------------------------------------------------------------------

@app.get("/api/plantillas")
def listar_plantillas():
    resumen = []

    if os.path.isdir(PLANTILLAS_DIR):
        for archivo in os.listdir(PLANTILLAS_DIR):
            if not archivo.endswith(".json"):
                continue

            pid = archivo[:-5]
            plantilla = leer_plantilla(pid)

            if not plantilla:
                continue

            resumen.append({
                "id": plantilla.get("id", pid),
                "nombre": plantilla.get("nombre", ""),
                "miniatura": plantilla.get("miniatura", ""),
                "actualizado": plantilla.get("actualizado", ""),
            })

    resumen.sort(key=lambda p: p["actualizado"], reverse=True)

    return jsonify(resumen)


@app.get("/api/plantillas/<pid>")
def obtener_plantilla(pid):
    plantilla = leer_plantilla(pid)

    if plantilla is None:
        return jsonify(error="Plantilla no encontrada."), 404

    return jsonify(plantilla)


@app.post("/api/plantillas")
def guardar_plantilla():
    datos = request.get_json(silent=True) or {}

    nombre = str(datos.get("nombre", "")).strip()[:80]
    lienzo = datos.get("lienzo")
    miniatura = datos.get("miniatura", "")

    try:
        ancho = int(datos.get("ancho"))
        alto = int(datos.get("alto"))
    except (TypeError, ValueError):
        return jsonify(error="Tamaño de lienzo inválido."), 400

    if not nombre:
        return jsonify(error="La plantilla necesita un nombre."), 400

    if (
        not isinstance(lienzo, dict)
        or not isinstance(lienzo.get("objects"), list)
    ):
        return jsonify(error="El diseño no tiene el formato esperado."), 400

    if not (200 <= ancho <= 4000 and 200 <= alto <= 4000):
        return jsonify(error="Tamaño de lienzo fuera de rango."), 400

    if (
        not isinstance(miniatura, str)
        or not miniatura.startswith("data:image/")
        or len(miniatura) > 300_000
    ):
        miniatura = ""

    pid = datos.get("id")
    ruta = ruta_plantilla(pid)
    existe = bool(ruta and os.path.isfile(ruta))

    if not existe:
        pid = uuid4().hex

    os.makedirs(PLANTILLAS_DIR, exist_ok=True)

    escribir_json(ruta_plantilla(pid), {
        "id": pid,
        "nombre": nombre,
        "ancho": ancho,
        "alto": alto,
        "lienzo": lienzo,
        "miniatura": miniatura,
        "actualizado": datetime.now(timezone.utc).isoformat(),
    })

    return jsonify(id=pid, nombre=nombre), (200 if existe else 201)


@app.delete("/api/plantillas/<pid>")
def eliminar_plantilla(pid):
    ruta = ruta_plantilla(pid)

    if not ruta or not os.path.isfile(ruta):
        return jsonify(error="Plantilla no encontrada."), 404

    os.remove(ruta)

    return jsonify(ok=True)


# -------------------------------------------------------------------
# API DE CÓDIGOS DE PAÍS
# -------------------------------------------------------------------

@app.get("/api/countries")
def get_countries():
    """Devuelve la lista de países desde el archivo JSON local"""
    return jsonify(PAISES_DISPONIBLES)
# -------------------------------------------------------------------
# INICIO
# -------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)