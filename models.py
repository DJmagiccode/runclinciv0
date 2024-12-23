from db import db

class Clinic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    head_doctor = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    photo = db.Column(db.String(100), nullable=True)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    blood_group = db.Column(db.String(5), nullable=False)
    emergency_contact = db.Column(db.String(20), nullable=False)
    photo = db.Column(db.String(100), nullable=True)