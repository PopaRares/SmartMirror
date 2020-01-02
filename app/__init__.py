from flask import Flask
from flask_sqlalchemy import SQLAlchemy

shared = {
    "face": False,
    "face_id": 0
}

app = Flask(__name__)
app.static_folder = 'static'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../DB/mirror.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes, user
