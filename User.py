from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_time = db.Column(db.Integer)
    username = db.Column(db.String())
