from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    todos = db.relationship('Todos')

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    location = db.Column(db.String(200))
    notes = db.Column(db.String(2000))
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    status = db.Column(db.String(50))  # Add a status field
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


