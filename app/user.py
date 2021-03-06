from app import db
import json


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name
