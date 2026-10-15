import json
import os
import re
from datetime import datetime, timezone
from uuid import uuid4
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
# Las imágenes subidas al editor viajan dentro del JSON de la plantilla
app.config["MAX_CONTENT_LENGTH"] = 12 * 1024 * 1024

# Todo se guarda junto a app.py, sin importar desde dónde ejecutes Flask
BASE = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE, "contactos.json")
PLANTILLAS_DIR = os.path.join(BASE, "plantillas")
ID_RE = re.compile(r"^[0-9a-f]{32}$")


# ---------------------------------------------------------------- utilidades
def escribir_json(ruta, datos):
    # Se escribe en un archivo temporal y luego se reemplaza, para no corromper el JSON
    tmp = ruta + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    os.replace(tmp, ruta)


def cargar_contactos():
    try:
        with open(ARCHIVO, encoding="utf-8") as f:
            contactos = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    # Compatibilidad: contactos guardados antes, sin id
    if any("id" not in c for c in contactos):
        for c in contactos:
            c.setdefault("id", uuid4().hex)
            c.setdefault("link", "")
        guardar_contactos(contactos)
    return contactos


def guardar_contactos(contactos):
    escribir_json(ARCHIVO, contactos)


def ruta_plantilla(pid):
    """Ruta del archivo de una plantilla, o None si el id no es válido (evita rutas raras)."""
    if not isinstance(pid, str) or not ID_RE.match(pid):
        return None
    return os.path.join(PLANTILLAS_DIR, pid + ".json")


def leer_plantilla(pid):
    ruta = ruta_plantilla(pid)
    if not ruta:
        return None
    try:
        with open(ruta, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


# ------------------------------------------------------------------- páginas
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


# ---------------------------------------------------------- API de contactos
@app.get("/api/contactos")
def listar():
    return jsonify(cargar_contactos())


@app.post("/api/contactos")
def crear():
    datos = request.get_json(silent=True) or {}
    nombre = str(datos.get("nombre", "")).strip()
    telefono = "".join(c for c in str(datos.get("telefono", "")) if c.isdigit())
    link = str(datos.get("link", "")).strip()

    if not nombre:
        return jsonify(error="El nombre es obligatorio."), 400
    if not 8 <= len(telefono) <= 15:
        return jsonify(error="El teléfono debe tener entre 8 y 15 dígitos, con código de país."), 400
    if link and not link.startswith(("http://", "https://")):
        return jsonify(error="El link debe empezar con http:// o https://"), 400

    contactos = cargar_contactos()
    if any(c["telefono"] == telefono for c in contactos):
        return jsonify(error="Ese teléfono ya está en tu lista."), 409

    nuevo = {"id": uuid4().hex, "nombre": nombre, "telefono": telefono, "link": link}
    contactos.append(nuevo)
    guardar_contactos(contactos)
    return jsonify(nuevo), 201


@app.delete("/api/contactos/<contacto_id>")
def eliminar(contacto_id):
    contactos = cargar_contactos()
    restantes = [c for c in contactos if c["id"] != contacto_id]
    if len(restantes) == len(contactos):
        return jsonify(error="Contacto no encontrado."), 404
    guardar_contactos(restantes)
    return jsonify(ok=True)


# ---------------------------------------------------------- API de plantillas
@app.get("/api/plantillas")
def listar_plantillas():
    resumen = []
    if os.path.isdir(PLANTILLAS_DIR):
        for archivo in os.listdir(PLANTILLAS_DIR):
            if not archivo.endswith(".json"):
                continue
            p = leer_plantilla(archivo[:-5])
            if p:
                resumen.append({
                    "id": p["id"],
                    "nombre": p["nombre"],
                    "miniatura": p.get("miniatura", ""),
                    "actualizado": p.get("actualizado", ""),
                })
    resumen.sort(key=lambda p: p["actualizado"], reverse=True)
    return jsonify(resumen)


@app.get("/api/plantillas/<pid>")
def obtener_plantilla(pid):
    p = leer_plantilla(pid)
    if p is None:
        return jsonify(error="Plantilla no encontrada."), 404
    return jsonify(p)


@app.post("/api/plantillas")
def guardar_plantilla():
    d = request.get_json(silent=True) or {}
    nombre = str(d.get("nombre", "")).strip()[:80]
    lienzo = d.get("lienzo")
    miniatura = d.get("miniatura", "")

    try:
        ancho, alto = int(d.get("ancho")), int(d.get("alto"))
    except (TypeError, ValueError):
        return jsonify(error="Tamaño de lienzo inválido."), 400

    if not nombre:
        return jsonify(error="La plantilla necesita un nombre."), 400
    if not isinstance(lienzo, dict) or not isinstance(lienzo.get("objects"), list):
        return jsonify(error="El diseño no tiene el formato esperado."), 400
    if not (200 <= ancho <= 4000 and 200 <= alto <= 4000):
        return jsonify(error="Tamaño de lienzo fuera de rango."), 400
    if not isinstance(miniatura, str) or not miniatura.startswith("data:image/") or len(miniatura) > 300_000:
        miniatura = ""

    # Si viene un id existente se actualiza; si no, se crea una plantilla nueva
    pid = d.get("id")
    existe = bool(ruta_plantilla(pid)) and os.path.exists(ruta_plantilla(pid))
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
    if not ruta or not os.path.exists(ruta):
        return jsonify(error="Plantilla no encontrada."), 404
    os.remove(ruta)
    return jsonify(ok=True)


if __name__ == "__main__":
    app.run(debug=True)