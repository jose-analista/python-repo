
import requests

from typing import Any

# URLs de las API de Open-Meteo
URL_GEOCODING = "https://geocoding-api.open-meteo.com/v1/search"
URL_CLIMA = "https://api.open-meteo.com/v1/forecast"

TIMEOUT = 10

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


def buscar_ciudad(ciudad: str) -> list[dict[str, Any]]:
    """Busca ciudades y devuelve sus datos geográficos."""

    parametros = {
        "name": ciudad,
        "count": 5,
        "language": "es",
        "format": "json",
    }

    respuesta = requests.get(
        URL_GEOCODING,
        params=parametros,
        timeout=TIMEOUT,
    )
    respuesta.raise_for_status()

    datos = respuesta.json()
    return datos.get("results", [])


def consultar_clima(
    latitud: float,
    longitud: float,
) -> dict[str, Any]:
    """Obtiene las condiciones meteorológicas actuales."""

    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "wind_speed_10m,"
            "weather_code"
        ),
        "timezone": "auto",
    }

    respuesta = requests.get(
        URL_CLIMA,
        params=parametros,
        timeout=TIMEOUT,
    )
    respuesta.raise_for_status()

    datos = respuesta.json()
    return datos["current"]


def seleccionar_ciudad(
    ciudades: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """Permite elegir una ciudad entre varios resultados."""

    if not ciudades:
        print("No se encontraron ciudades.")
        return None

    for indice, ciudad in enumerate(ciudades, start=1):
        pais = ciudad.get("country", "País desconocido")
        region = ciudad.get("admin1", "")
        print(f"{indice}. {ciudad['name']} - {region}, {pais}")

    while True:
        opcion = input(
            "Selecciona una ciudad (0 para cancelar): "
        ).strip()

        if opcion == "0":
            return None

        if opcion.isdigit():
            numero = int(opcion)

            if 1 <= numero <= len(ciudades):
                return ciudades[numero - 1]

        print("Opción no válida. Inténtalo nuevamente.")


def mostrar_clima(
    ubicacion: dict[str, Any],
    clima: dict[str, Any],
) -> None:
    """Muestra el resumen meteorológico."""

    codigo = clima.get("weather_code")
    descripcion = CODIGOS_CLIMA.get(
        codigo,
        "Condición meteorológica desconocida",
    )

    print("\n" + "=" * 35)
    print("       CONSULTA DEL CLIMA")
    print("=" * 35)
    print(f"Ciudad: {ubicacion['name']}")
    print(f"País: {ubicacion.get('country', 'No disponible')}")
    print(f"Condición: {descripcion}")
    print(f"Temperatura: {clima['temperature_2m']} °C")
    print(f"Humedad: {clima['relative_humidity_2m']} %")
    print(f"Viento: {clima['wind_speed_10m']} km/h")
    print(f"Hora local: {clima['time']}")
    print("=" * 35)


def main() -> None:
    """Coordina la ejecución del programa."""

    ciudad = input("Ingresa una ciudad: ").strip()

    if not ciudad:
        print("Debes ingresar el nombre de una ciudad.")
        return

    try:
        ciudades = buscar_ciudad(ciudad)
        ubicacion = seleccionar_ciudad(ciudades)

        if ubicacion is None:
            return

        clima = consultar_clima(
            ubicacion["latitude"],
            ubicacion["longitude"],
        )

        mostrar_clima(ubicacion, clima)

    except requests.exceptions.Timeout:
        print("La consulta tardó demasiado. Inténtalo nuevamente.")

    except requests.exceptions.HTTPError as error:
        print(f"Error HTTP al consultar la API: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Error de conexión: {error}")

    except (KeyError, ValueError, TypeError):
        print("La API devolvió datos inesperados.")


if __name__ == "__main__":
    main()