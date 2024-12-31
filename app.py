from flask import Flask, render_template, redirect, url_for, request, flash, session
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
from functools import wraps
from forms import RegistrationForm, ClinicForm, LoginForm, RegisterForm
from models import Clinic, Patient, User
from db import db
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
    return {'db': db, 'Clinic': Clinic, 'Patient': Patient, 'User': User}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))
    form = LoginForm()
    register_form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            return redirect(url_for('index'))
        flash('Invalid username or password', 'error')
    return render_template('login.html', form=form, register_form=register_form)

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()
    register_form = RegisterForm()
    try:
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
    except Exception as e:
        logging.error(f"Exception during user registration: {e}")
        flash('An error occurred during registration. Please try again.', 'error')
    return render_template('register_user.html', form=form, register_form=register_form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/clinics', methods=['GET', 'POST'])
@login_required
def clinics():
    user_id = session['user_id']
    clinics = Clinic.query.filter_by(owner_id=user_id).all()
    return render_template('clinics.html', clinics=clinics)

@app.route('/add_clinic', methods=['GET', 'POST'])
@login_required
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
            owner_id=session['user_id'],
            head_doctor=form.head_doctor.data,
            address=form.address.data,
            photo=photo_filename
        )
        db.session.add(clinic)
        db.session.commit()
        return redirect(url_for('clinics'))
    return render_template('add_clinic.html', form=form)

@app.route('/clinic/<int:clinic_id>')
@login_required
def clinic_home(clinic_id):
    clinic = Clinic.query.get_or_404(clinic_id)
    session['clinic_id'] = clinic_id
    return render_template('clinic_home.html', clinic=clinic)

@app.route('/clinic/<int:clinic_id>/register', methods=['GET', 'POST'])
@login_required
def register_patient(clinic_id):
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_patient = Patient.query.filter_by(contact=form.contact.data, user_id=session['user_id']).first()
        if existing_patient:
            flash('A patient with this contact number already exists.', 'error')
            return redirect(url_for('register_patient', clinic_id=clinic_id))
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
            photo=photo_filename,
            clinic_id=clinic_id,
            user_id=session['user_id']  # Set user_id to the logged-in user
        )
        db.session.add(patient)
        db.session.commit()
        flash('Patient registered successfully.', 'success')
        return redirect(url_for('clinic_home', clinic_id=clinic_id))
    return render_template('registration.html', form=form)

@app.route('/doctor_home')
@login_required
def doctor_home():
    return render_template('doctor_home.html')

@app.route('/patients')
@login_required
def patients():
    search = request.args.get('search')
    user_id = session['user_id']
    if search:
        patients = Patient.query.filter(
            (Patient.user_id == user_id) &
            (Patient.first_name.contains(search) |
            Patient.last_name.contains(search) |
            Patient.address.contains(search) |
            Patient.contact.contains(search) |
            Patient.email.contains(search) |
            Patient.age.contains(search) |
            Patient.sex.contains(search) |
            Patient.blood_group.contains(search) |
            Patient.emergency_contact.contains(search))
        ).all()
    else:
        patients = Patient.query.filter_by(user_id=user_id).all()
    return render_template('patients.html', patients=patients)

@app.route('/patient/<int:patient_id>')
@login_required
def patient_detail(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    return render_template('patient_detail.html', patient=patient)

@app.route('/patient/<int:patient_id>/modify', methods=['GET', 'POST'])
@login_required
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
@login_required
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

app.config['SESSION_COOKIE_SECURE'] = True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
