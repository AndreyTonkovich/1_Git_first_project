from db import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    age = db.Column(db.Float, nullable=False)
    owner_name = db.Column(db.String(250), nullable=False)