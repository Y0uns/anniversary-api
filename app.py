from flask import Flask, jsonify, send_file, render_template
from datetime import datetime
import os

app = Flask(__name__)

# Configuración personalizada
FIRST_DATE = "2024-06-02"  # Cambia por tu fecha real
PARTNER_NAME = "Amorcito"  # Nombre de tu pareja
YOUR_NAME = "Tu Amorcito"     # Tu nombre

# Función para calcular días juntos
def calculate_days_together():
    first_day = datetime.strptime(FIRST_DATE, "%Y-%m-%d")
    today = datetime.now()
    return (today - first_day).days

# Reproducir música en segundo plano (solo en local)
def play_music():
    playsound("static/song.mp3")

# Endpoints de la API
@app.route('/')
def home():
    return jsonify({
        "message": f"¡Hola {PARTNER_NAME}! Bienvenido/a a nuestra API del amor.",
        "endpoints": {
            "anniversary": "/anniversary",
            "love_letter": "/love_letter",
            "photo": "/photo",
            "audio": "/audio",
            "web": "/home"  # Página con música
        }
    })

@app.route('/anniversary')
def anniversary():
    return render_template('anniversary.html',
                         partner_name=PARTNER_NAME,
                         days_together=calculate_days_together(),
                         first_date=FIRST_DATE,
                         secret_code="TEAMO<3")

@app.route('/home')
def home_page():
    return render_template('index.html', your_name=YOUR_NAME)

# Archivos estáticos (foto, audio)
@app.route('/photo')
def photo():
    return send_file("static/photo.jpg", mimetype='image/jpg')
@app.route('/fotito')
def foto():
    return send_file("static/fotito.jpg", mimetype='image/jpg')
@app.route('/halloween')
def jalowin():
    return send_file("static/halloween.jpg", mimetype='image/jpg')
@app.route('/comida')
def comida():
    return send_file("static/comida.jpg", mimetype='image/jpg')
@app.route('/maitencillo')
def maitencillo():
    return send_file("static/maitencillo.jpg", mimetype='image/jpg')
@app.route('/audio')
def audio():
    return send_file("static/love_audio.mp3", mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)