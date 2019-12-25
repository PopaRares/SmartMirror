from threading import Thread

from flask import render_template

from app import app

data = {'isFace': 0}


@app.route('/')
@app.route('/mirror')
def index():
    user = {"username": "Rares"}
    return render_template('mirror.html', data=data, user=user)


@app.route("/getFace", methods=['GET'])
def getFace():
    return data
