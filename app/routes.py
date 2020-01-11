from threading import Thread
from flask import render_template
from app import app, Shared
from datetime import datetime

data = {}


@app.route('/')
@app.route('/mirror')
def index():
    return render_template('mirror.html', font_url="https://fonts.googleapis.com/css?family=Montserrat&display=swap")


@app.route("/getFace", methods=['GET'])
def getFace():
    data['isFace'] = Shared.FACE_EXISTS
    #data['user'] = Shared.CURRENT_USER
    return data
