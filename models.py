from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    ingredients = db.Column(db.String, nullable=False)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    review = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer, nullable=False)