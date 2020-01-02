from threading import Thread

from flask import render_template

from app import app, shared


data = {'isFace': False}


@app.route('/')
@app.route('/mirror')
def index():
    user = {"username": "1"}
    return render_template('mirror.html', data=data, user=user)


@app.route("/getFace", methods=['GET'])
def getFace():
    data['isFace'] = shared['face']
    return data
