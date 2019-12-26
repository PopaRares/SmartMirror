from threading import Thread

from flask import render_template

from app import app

import shared_data as shared

data = {'isFace': False}


@app.route('/')
@app.route('/mirror')
def index():
    user = {"username": "Rares"}
    return render_template('mirror.html', data=data, user=user)


@app.route("/getFace", methods=['GET'])
def getFace():
    data['isFace'] = shared.face
    return data
