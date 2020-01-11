from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.configuration import Config
from app.shared import Shared

app = Flask(__name__)
app.static_folder = 'static'

app.config.from_object(Config)

db = SQLAlchemy(app)

from app import routes, user
