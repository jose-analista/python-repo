import json
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError

with open("puntos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

geolocalizador = Nominatim(
    user_agent="autofaro"
)

semaforos = datos["semaforo"]

for nombre, coordenadas in list(semaforos.items())[:10]:

    latitud = coordenadas["latitud"]
    longitud = coordenadas["longitud"]

    print(f"\nSemáforo: {nombre}")
    print(f"Coordenadas: {latitud}, {longitud}")

    try:
        ubicacion = geolocalizador.reverse(
            (latitud, longitud),
            language="es",
            zoom=18,
            exactly_one=True,
            timeout=15
        )

        if ubicacion:
            print("Dirección encontrada:", ubicacion.address)
        else:
            print("No se encontró una dirección.")

    except GeocoderServiceError as error:
        print("Error de consulta:", error)

    # Respetar el límite del servicio público
    time.sleep(1.1)