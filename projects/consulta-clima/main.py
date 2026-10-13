
# Importamos requests para realizar peticiones HTTP a las API.
import requests

# Any permite indicar que un diccionario puede contener distintos tipos
# de datos: cadenas, números, listas, etc.
from typing import Any


# ============================================================
# 1. CONFIGURACIÓN DEL PROGRAMA
# ============================================================

# API de geolocalización: permite buscar una ciudad y obtener
# sus coordenadas geográficas (latitud y longitud).
URL_GEOCODING = "https://geocoding-api.open-meteo.com/v1/search"

# API meteorológica: permite consultar el clima usando coordenadas.
URL_CLIMA = "https://api.open-meteo.com/v1/forecast"

# Tiempo máximo de espera de cada petición HTTP, en segundos.
# Si la API tarda más de 10 segundos, se genera un error de timeout.
TIMEOUT = 10

# Diccionario que relaciona los códigos meteorológicos de Open-Meteo
# con descripciones fáciles de entender.
# La clave es el código numérico y el valor es el texto mostrado.
CODIGOS_CLIMA = {
    0: "Despejado",
    1: "Mayormente despejado",
    2: "Parcialmente nublado",
    3: "Nublado",
    45: "Niebla",
    48: "Niebla con escarcha",
    51: "Llovizna ligera",
    53: "Llovizna moderada",
    55: "Llovizna intensa",
    61: "Lluvia ligera",
    63: "Lluvia moderada",
    65: "Lluvia intensa",
    71: "Nevada ligera",
    73: "Nevada moderada",
    75: "Nevada intensa",
    80: "Chubascos ligeros",
    81: "Chubascos moderados",
    82: "Chubascos intensos",
    95: "Tormenta eléctrica",
    96: "Tormenta con granizo ligero",
    99: "Tormenta con granizo intenso",
}


# ============================================================
# 2. BUSCAR UNA CIUDAD
# ============================================================

def buscar_ciudad(ciudad: str) -> list[dict[str, Any]]:
    """
    Busca una ciudad utilizando la API de geolocalización.

    Parámetro:
        ciudad: nombre de la ciudad ingresada por el usuario.

    Retorna:
        Una lista de diccionarios con los resultados encontrados.
        Cada diccionario contiene datos como nombre, país y coordenadas.
    """

    # Parámetros que enviaremos a la API.
    parametros = {
        "name": ciudad,     # Nombre que queremos buscar.
        "count": 5,         # Máximo de cinco resultados.
        "language": "es",   # Solicitar resultados en español.
        "format": "json",   # Recibir la respuesta en formato JSON.
    }

    # Realizamos una petición GET a la API.
    # params agrega los parámetros a la URL automáticamente.
    # timeout evita que el programa espere indefinidamente.
    respuesta = requests.get(
        URL_GEOCODING,
        params=parametros,
        timeout=TIMEOUT,
    )

    # Si el servidor responde con un error HTTP, lo detectamos.
    # Por ejemplo, un error 404 o 500.
    respuesta.raise_for_status()

    # Convertimos el JSON recibido en estructuras de datos Python.
    datos = respuesta.json()

    # Obtenemos la lista de ciudades encontrada.
    # Si no existe la clave "results", devolvemos una lista vacía.
    return datos.get("results", [])


# ============================================================
# 2.5. OBTENER UBICACIÓN ACTUAL
# ============================================================

def obtener_ubicacion_actual() -> dict[str, Any] | None:
    """
    Obtiene la ubicación aproximada del usuario basada en su dirección IP.
    """
    # Usamos ip-api.com, que es más permisivo con scripts de Python
    url_ip = "http://ip-api.com/json/"
    
    try:
        respuesta = requests.get(url_ip, timeout=TIMEOUT)
        respuesta.raise_for_status()
        datos = respuesta.json()
        
        # Esta API devuelve "status": "success" si funcionó correctamente
        if datos.get("status") != "success":
            print(f"⚠️ La API de ubicación respondió con error: {datos.get('message')}")
            return None
        
        # Nota: esta API usa "lat" y "lon" en lugar de "latitude" y "longitude"
        return {
            "name": datos.get("city", "Ubicación desconocida"),
            "country": datos.get("country", "País desconocido"),
            "latitude": datos.get("lat"),
            "longitude": datos.get("lon"),
        }
        
    except requests.exceptions.RequestException as error:
        # Ahora imprimimos el error real para saber qué pasa
        print(f"⚠️ Error de conexión al obtener ubicación: {error}")
        return None

# ============================================================
# 3. CONSULTAR EL CLIMA
# ============================================================

def consultar_clima(
    latitud: float,
    longitud: float,
) -> dict[str, Any]:
    """
    Consulta el clima actual de unas coordenadas geográficas.

    Parámetros:
        latitud: posición norte-sur de la ubicación.
        longitud: posición este-oeste de la ubicación.

    Retorna:
        Un diccionario con temperatura, humedad, viento,
        código meteorológico y hora de medición.
    """

    # Indicamos a la API qué ubicación y datos necesitamos.
    parametros = {
        "latitude": latitud,
        "longitude": longitud,

        # Solicitamos las variables meteorológicas actuales.
        # Las comas separan los nombres de las variables.
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "wind_speed_10m,"
            "weather_code"
        ),

        # La API selecciona la zona horaria correspondiente
        # a las coordenadas consultadas.
        "timezone": "auto",
    }

    # Enviamos la petición a la API meteorológica.
    respuesta = requests.get(
        URL_CLIMA,
        params=parametros,
        timeout=TIMEOUT,
    )

    # Detenemos el flujo si existe un error HTTP.
    respuesta.raise_for_status()

    # Convertimos la respuesta JSON en un diccionario Python.
    datos = respuesta.json()

    # Devolvemos solamente los datos del clima actual.
    return datos["current"]


# ============================================================
# 4. SELECCIONAR UNA CIUDAD
# ============================================================

def seleccionar_ciudad(
    ciudades: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """
    Muestra las ciudades encontradas y permite elegir una.

    Parámetro:
        ciudades: lista devuelta por buscar_ciudad().

    Retorna:
        El diccionario de la ciudad seleccionada.
        Retorna None si no hay resultados o si el usuario cancela.
    """

    # Una lista vacía significa que no encontramos coincidencias.
    if not ciudades:
        print("No se encontraron ciudades.")
        return None

    # enumerate permite recorrer la lista con un contador.
    # start=1 hace que las opciones comiencen desde el número 1.
    for indice, ciudad in enumerate(ciudades, start=1):

        # get() permite usar un valor alternativo si falta una clave.
        pais = ciudad.get("country", "País desconocido")
        region = ciudad.get("admin1", "")

        # Mostramos el nombre, la región y el país.
        print(f"{indice}. {ciudad['name']} - {region}, {pais}")

    # Repetimos la pregunta hasta que la selección sea válida.
    while True:
        opcion = input(
            "Selecciona una ciudad (0 para cancelar): "
        ).strip()

        # El usuario puede cancelar escribiendo cero.
        if opcion == "0":
            return None

        # isdigit() comprueba que la entrada contenga dígitos.
        if opcion.isdigit():
            numero = int(opcion)

            # Comprobamos que el número esté dentro del rango válido.
            if 1 <= numero <= len(ciudades):

                # Las listas empiezan en el índice 0.
                # Por eso restamos 1 al número elegido.
                return ciudades[numero - 1]

        # Si la entrada no es válida, volvemos a preguntar.
        print("Opción no válida. Inténtalo nuevamente.")


# ============================================================
# 5. MOSTRAR LOS RESULTADOS DEL CLIMA
# ============================================================

def mostrar_clima(
    ubicacion: dict[str, Any],
    clima: dict[str, Any],
) -> None:
    """
    Presenta los datos meteorológicos de manera legible.

    Parámetros:
        ubicacion: información de la ciudad seleccionada.
        clima: información meteorológica recibida de la API.

    Retorna:
        None, porque solamente muestra información en pantalla.
    """

    # Obtenemos el código meteorológico del diccionario.
    codigo = clima.get("weather_code")

    # Buscamos su descripción en CODIGOS_CLIMA.
    # Si el código no está registrado, mostramos un texto alternativo.
    descripcion = CODIGOS_CLIMA.get(
        codigo,
        "Condición meteorológica desconocida",
    )

    # Mostramos un encabezado para organizar la salida.
    print("\n" + "=" * 35)
    print("       CONSULTA DEL CLIMA")
    print("=" * 35)

    # Mostramos los datos de la ciudad.
    print(f"Ciudad: {ubicacion['name']}")
    print(f"País: {ubicacion.get('country', 'No disponible')}")

    # Mostramos los datos meteorológicos.
    print(f"Condición: {descripcion}")
    print(f"Temperatura: {clima['temperature_2m']} °C")
    print(f"Humedad: {clima['relative_humidity_2m']} %")
    print(f"Viento: {clima['wind_speed_10m']} km/h")
    print(f"Hora local: {clima['time']}")

    print("=" * 35)


# ============================================================
# 6. FUNCIÓN PRINCIPAL
# ============================================================

def main() -> None:
    """
    Coordina el flujo completo del programa, permitiendo
    elegir entre ubicación automática o búsqueda manual.
    """
    print("\n--- CONSULTA DEL CLIMA ---")
    print("1. Usar mi ubicación actual (automático)")
    print("2. Buscar una ciudad manualmente")
    
    opcion = input("Elige una opción (1 o 2): ").strip()
    
    ubicacion = None

    if opcion == "1":
        # Flujo automático por IP
        print("📍 Detectando ubicación...")
        ubicacion = obtener_ubicacion_actual()
        if ubicacion is None:
            print("No se pudo obtener la ubicación. Saliendo del programa.")
            return
            
    else:
        # Flujo manual (tu código original)
        ciudad = input("Ingresa el nombre de una ciudad: ").strip()
        if not ciudad:
            print("Debes ingresar el nombre de una ciudad.")
            return
            
        try:
            ciudades = buscar_ciudad(ciudad)
            ubicacion = seleccionar_ciudad(ciudades)
            if ubicacion is None:
                return
        except requests.exceptions.RequestException as error:
            print(f"Error de conexión al buscar la ciudad: {error}")
            return

    # ============================================================
    # A PARTIR DE AQUÍ, EL FLUJO ES EL MISMO PARA AMBAS OPCIONES
    # ============================================================
    
    try:
        # Paso 3: consultamos el clima usando las coordenadas
        clima = consultar_clima(
            ubicacion["latitude"],
            ubicacion["longitude"],
        )

        # Paso 4: presentamos el resultado al usuario
        mostrar_clima(ubicacion, clima)

    except requests.exceptions.Timeout:
        print("La consulta del clima tardó demasiado. Inténtalo nuevamente.")
    except requests.exceptions.HTTPError as error:
        print(f"Error HTTP al consultar el clima: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Error de conexión: {error}")
    except (KeyError, ValueError, TypeError):
        print("La API devolvió datos inesperados.")


if __name__ == "__main__":
    main()
# ============================================================
# 7. PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

# Esta condición comprueba si el archivo se está ejecutando
# directamente, en lugar de ser importado desde otro módulo.
#
# Si ejecutamos:
# python3 main.py
#
# se llama a main() y comienza el programa.
if __name__ == "__main__":
    main()