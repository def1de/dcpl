import datetime
from .extentions import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120))

class Passwords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String)
    name = db.Column(db.String)
    data_paths = db.Column(db.String)