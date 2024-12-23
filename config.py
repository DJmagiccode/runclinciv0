import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///medical_clinic.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False