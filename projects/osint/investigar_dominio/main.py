
import json
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.parse import urlencode

def investigar_dominio(dominio):
    dominio = dominio.strip().lower()

    if not dominio or "/" in dominio or " " in dominio:
        raise ValueError("Introduce un dominio válido.")

    parametros = urlencode({
        "q": f"%.{dominio}",
        "output": "json"
    })

    url = f"https://crt.sh/?{parametros}"
    solicitud = Request(
        url,
        headers={"User-Agent": "Caytech-OSINT-Educativo/1.0"}
    )

    with urlopen(solicitud, timeout=20) as respuesta:
        certificados = json.load(respuesta)

    nombres = set()

    for certificado in certificados:
        for nombre in certificado.get("name_value", "").splitlines():
            nombre = nombre.strip().lower().lstrip("*.")
            if nombre == dominio or nombre.endswith("." + dominio):
                nombres.add(nombre)

    informe = {
        "dominio_consultado": dominio,
        "fecha_utc": datetime.now(timezone.utc).isoformat(),
        "fuente": url,
        "total_nombres_unicos": len(nombres),
        "nombres": sorted(nombres)
    }

    with open("informe_osint.json", "w", encoding="utf-8") as archivo:
        json.dump(informe, archivo, ensure_ascii=False, indent=2)

    return informe


if __name__ == "__main__":
    dominio = input("Dominio autorizado: ")

    try:
        resultado = investigar_dominio(dominio)
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
        print("\nInforme guardado en informe_osint.json")
    except Exception as error:
        print(f"No se pudo completar la consulta: {error}")
