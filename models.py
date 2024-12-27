from werkzeug.security import generate_password_hash, check_password_hash
from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    clinics = db.relationship('Clinic', backref='owner', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Clinic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    contact = db.Column(db.String(150), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_clinic_user'), nullable=False)  # Reapply NOT NULL
    head_doctor = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    photo = db.Column(db.String(150), nullable=True)
    patients = db.relationship('Patient', backref='clinic', lazy=True)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    contact = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    emergency_contact = db.Column(db.String(150), nullable=False)
    photo = db.Column(db.String(150), nullable=True)
    clinic_id = db.Column(db.Integer, db.ForeignKey('clinic.id', name='fk_patient_clinic'), nullable=False)