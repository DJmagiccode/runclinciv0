from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    age = IntegerField('Age', validators=[DataRequired()])
    sex = StringField('Sex', validators=[DataRequired()])
    blood_group = StringField('Blood Group', validators=[DataRequired()])
    emergency_contact = StringField('Emergency Contact', validators=[DataRequired()])
    photo = FileField('Upload Photo')
    submit = SubmitField('Submit')

class ClinicForm(FlaskForm):
    name = StringField('Clinic Name', validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired()])
    owner = StringField('Owner', validators=[DataRequired()])
    head_doctor = StringField('Head Doctor', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    photo = FileField('Upload Photo')
    submit = SubmitField('Add Clinic')