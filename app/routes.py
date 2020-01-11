from flask import render_template
from app import app, Shared
from app.user import User
import json
data = {}


@app.route('/')
@app.route('/mirror')
def index():
    return render_template('mirror.html', font_url="https://fonts.googleapis.com/css?family=Montserrat&display=swap")


@app.route("/getFace", methods=['GET'])
def getFace():
    data['isFace'] = Shared.FACE_EXISTS
    if Shared.CURRENT_USER is None:
        data['name'] = "stranger"
    else:
        data['name'] = Shared.CURRENT_USER.name
    return data
