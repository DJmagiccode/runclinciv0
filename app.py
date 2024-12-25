from flask import Flask, render_template, redirect, url_for, request, flash, session
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
from forms import RegistrationForm, ClinicForm
from db import db
from models import Clinic, Patient
import os
import logging

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

migrate = Migrate(app, db)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set up logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Clinic': Clinic, 'Patient': Patient}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clinics', methods=['GET', 'POST'])
def clinics():
    clinics = Clinic.query.all()
    return render_template('clinics.html', clinics=clinics)

@app.route('/add_clinic', methods=['GET', 'POST'])
def add_clinic():
    form = ClinicForm()
    if form.validate_on_submit():
        photo_filename = None
        if form.photo.data:
            photo_filename = secure_filename(form.photo.data.filename)
            form.photo.data.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
        clinic = Clinic(
            name=form.name.data,
            contact=form.contact.data,
            owner=form.owner.data,
            head_doctor=form.head_doctor.data,
            address=form.address.data,
            photo=photo_filename
        )
        db.session.add(clinic)
        db.session.commit()
        return redirect(url_for('clinics'))
    return render_template('add_clinic.html', form=form)

@app.route('/clinic/<int:clinic_id>')
def clinic_home(clinic_id):
    clinic = Clinic.query.get_or_404(clinic_id)
    session['clinic_id'] = clinic_id
    return render_template('clinic_home.html', clinic=clinic)

@app.route('/clinic/<int:clinic_id>/register', methods=['GET', 'POST'])
def register(clinic_id):
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_patient = Patient.query.filter_by(contact=form.contact.data).first()
        if existing_patient:
            flash('A patient with this contact number already exists.', 'error')
            return redirect(url_for('register', clinic_id=clinic_id))
        photo_filename = None
        if form.photo.data:
            photo_filename = secure_filename(form.photo.data.filename)
            form.photo.data.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
        patient = Patient(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            address=form.address.data,
            contact=form.contact.data,
            email=form.email.data,
            age=form.age.data,
            sex=form.sex.data,
            blood_group=form.blood_group.data,
            emergency_contact=form.emergency_contact.data,
            photo=photo_filename
        )
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('clinic_home', clinic_id=clinic_id))
    return render_template('registration.html', form=form)

@app.route('/doctor_home')
def doctor_home():
    return render_template('doctor_home.html')

@app.route('/patients')
def patients():
    search = request.args.get('search')
    if search:
        patients = Patient.query.filter(
            Patient.first_name.contains(search) |
            Patient.last_name.contains(search) |
            Patient.address.contains(search) |
            Patient.contact.contains(search) |
            Patient.email.contains(search) |
            Patient.age.contains(search) |
            Patient.sex.contains(search) |
            Patient.blood_group.contains(search) |
            Patient.emergency_contact.contains(search)
        ).all()
    else:
        patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

@app.route('/patient/<int:patient_id>')
def patient_detail(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    return render_template('patient_detail.html', patient=patient)

@app.route('/patient/<int:patient_id>/modify', methods=['GET', 'POST'])
def modify_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    form = RegistrationForm(obj=patient)
    if form.validate_on_submit():
        if form.first_name.data:
            patient.first_name = form.first_name.data
        if form.last_name.data:
            patient.last_name = form.last_name.data
        if form.address.data:
            patient.address = form.address.data
        if form.contact.data:
            patient.contact = form.contact.data
        if form.email.data:
            patient.email = form.email.data
        if form.age.data:
            patient.age = form.age.data
        if form.sex.data:
            patient.sex = form.sex.data
        if form.blood_group.data:
            patient.blood_group = form.blood_group.data
        if form.emergency_contact.data:
            patient.emergency_contact = form.emergency_contact.data
        if form.photo.data:
            photo_filename = secure_filename(form.photo.data.filename)
            form.photo.data.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
            patient.photo = photo_filename
        db.session.commit()
        return redirect(url_for('patients'))
    return render_template('modify_patient.html', form=form, patient=patient)

@app.route('/patient/<int:patient_id>/delete', methods=['POST'])
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('patients'))

@app.errorhandler(500)
def internal_error(error):
    logging.error(f"Server Error: {error}, route: {request.url}")
    return "", 204

@app.errorhandler(Exception)
def unhandled_exception(e):
    logging.error(f"Unhandled Exception: {e}, route: {request.url}")
    return "", 204

if __name__ == '__main__':
    app.run(debug=True)