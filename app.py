from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

EMAIL_EMISOR = "stsdami@gmail.com"
EMAIL_PASSWORD = "ydff qrad ddpa puwd"
ARCHIVO_REGISTROS = "registros.txt"
ARCHIVO_PROCESADOS = "procesados.txt"

HTML_FORMULARIO = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Formulario de Registro</title>
  <style>
    body { font-family: Arial; background: #111; color: #0f0; text-align: center; padding: 2rem; }
    form { background: #222; display: inline-block; padding: 2rem; border-radius: 10px; box-shadow: 0 0 10px #0f0; }
    input, button { display: block; width: 100%; margin: 1rem 0; padding: 0.5rem; font-size: 1rem; }
    label { margin-top: 1rem; }
  </style>
</head>
<body>
  <h1>Registro</h1>
  <form method="POST">
    <label>Nombre:</label>
    <input type="text" name="nombre" required>
    <label>Correo Gmail:</label>
    <input type="email" name="email" required>
    <button type="submit">Registrarse</button>
  </form>
</body>
</html>
"""

def guardar_registro(nombre, email):
    entrada = f"Nombre: {nombre}\nEmail: {email}\n"
    with open(ARCHIVO_REGISTROS, "a") as f:
        f.write(entrada + "\n")
    with open(ARCHIVO_PROCESADOS, "a") as f:
        f.write(entrada + "\n")

def enviar_correo(nombre, destinatario):
    asunto = f"¡Bienvenido, {nombre}!"
    cuerpo = f"""
Hola {nombre},

Gracias por registrarte. Tu cuenta fue creada exitosamente.
Cualquier duda, podés contactarnos.

¡Saludos!
"""
    msg = MIMEMultipart()
    msg["From"] = EMAIL_EMISOR
    msg["To"] = destinatario
    msg["Subject"] = asunto
    msg.attach(MIMEText(cuerpo, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_EMISOR, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()

@app.route("/", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        guardar_registro(nombre, email)
        enviar_correo(nombre, email)
        return "<h2 style='color:lime'>¡Registro exitoso! Revisa tu correo.</h2>"
    return render_template_string(HTML_FORMULARIO)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
