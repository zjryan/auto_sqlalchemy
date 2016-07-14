from . import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_time = db.Column(db.Integer)
    name = db.Column(db.String())
    price = db.Column(db.Float)
    likes = db.Column(db.Integer)
    pic_url = db.Column(db.String())
