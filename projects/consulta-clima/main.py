
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
    Coordina el flujo completo del programa:
    entrada del usuario, búsqueda, consulta y presentación.
    """

    # Solicitamos una ciudad y eliminamos espacios al principio
    # y al final con strip().
    ciudad = input("Ingresa una ciudad: ").strip()

    # No continuamos si el usuario no escribió nada.
    if not ciudad:
        print("Debes ingresar el nombre de una ciudad.")
        return

    # try permite controlar errores que podrían ocurrir durante
    # las peticiones HTTP o al procesar los datos recibidos.
    try:

        # Paso 1: buscamos posibles coincidencias de la ciudad.
        ciudades = buscar_ciudad(ciudad)

        # Paso 2: permitimos elegir una de las coincidencias.
        ubicacion = seleccionar_ciudad(ciudades)

        # Si se cancela la selección, terminamos la función.
        if ubicacion is None:
            return

        # Paso 3: consultamos el clima usando las coordenadas
        # de la ciudad seleccionada.
        clima = consultar_clima(
            ubicacion["latitude"],
            ubicacion["longitude"],
        )

        # Paso 4: presentamos el resultado al usuario.
        mostrar_clima(ubicacion, clima)

    # Error: la petición superó el tiempo máximo de espera.
    except requests.exceptions.Timeout:
        print("La consulta tardó demasiado. Inténtalo nuevamente.")

    # Error: el servidor respondió con un estado HTTP de error.
    except requests.exceptions.HTTPError as error:
        print(f"Error HTTP al consultar la API: {error}")

    # Otros problemas de red, conexión o petición HTTP.
    except requests.exceptions.RequestException as error:
        print(f"Error de conexión: {error}")

    # Errores al acceder a claves o procesar valores inesperados.
    except (KeyError, ValueError, TypeError):
        print("La API devolvió datos inesperados.")


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