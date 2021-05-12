import datetime
from app import db, login
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from datetime import time

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    phone_number = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, name, username, phone_number, email, password):
        self.name = name
        self.phone_number = phone_number
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)