from urllib.parse import quote
from flask import Flask, render_template, request

app = Flask(__name__)

MENSAJE_BIENVENIDA = "¡Hola {nombre}! \U0001F44B Bienvenido/a. Gracias por contactarnos \U0001F60A ¿En qué te podemos ayudar?"
contactos = []


@app.route("/", methods=["GET", "POST"])
def index():
    enlace = None
    mensaje = None

    if request.method == "POST":
        print("FORM RECIBIDO:", dict(request.form))  # para depurar

        nombre = request.form.get("nombre", "").strip()
        link = request.form.get("link", "").strip()
        telefono = "".join(c for c in request.form.get("telefono", "") if c.isdigit())

        if nombre and telefono:
            mensaje = MENSAJE_BIENVENIDA.format(nombre=nombre)
            if link:
                mensaje += f" \U0001F517 Conoce más aquí: {link}"

            enlace = f"https://web.whatsapp.com/send?phone={telefono}&text={quote(mensaje)}"
            contactos.append({"nombre": nombre, "telefono": telefono})

    return render_template("index.html", enlace=enlace, mensaje=mensaje, contactos=contactos)


if __name__ == "__main__":
    app.run(debug=True)