from threading import Thread
from flask import render_template
from app import app, Shared
from datetime import datetime

data = {'isFace': False}

@app.route('/')
@app.route('/mirror')
def index():
    user = {'username': 'Rares'}
    date = datetime.now()
    return render_template('mirror.html', user=user, date=date, font_url="https://fonts.googleapis.com/css?family=Montserrat&display=swap")


@app.route("/getFace", methods=['GET'])
def getFace():
    data['isFace'] = Shared.FACE_EXISTS
    return data