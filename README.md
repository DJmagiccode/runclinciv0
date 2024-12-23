# Medical Clinic Portal

This is a web application for managing a medical clinic. It allows users to register patients, manage clinics, and view patient details.

## Features

- Add and manage clinics
- Register patients
- View and modify patient details
- Search for patients
- Doctor's dashboard

## Project Structure
pycache/ app.py config.py db.py dbinit.bat forms.py init_db.py instance/ models.py static/ styles.css uploads/ templates/ add_clinic.html clinic_home.html clinics.html doctor_home.html index.html modify_patient.html patient_detail.html patients.html registration.html


## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```sh
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. Run the application:
    ```sh
    flask run
    ```

## Configuration

The application configuration is defined in [config.py](http://_vscodecontentref_/17). The key configurations are:

- [SECRET_KEY](http://_vscodecontentref_/18): A secret key for the application.
- [SQLALCHEMY_DATABASE_URI](http://_vscodecontentref_/19): The database URI.
- [SQLALCHEMY_TRACK_MODIFICATIONS](http://_vscodecontentref_/20): Whether to track modifications of objects and emit signals.

## Database Models

The database models are defined in [models.py](http://_vscodecontentref_/21):

- [Clinic](http://_vscodecontentref_/22): Represents a clinic with fields for name, contact, owner, head doctor, address, and photo.
- [Patient](http://_vscodecontentref_/23): Represents a patient with fields for first name, last name, address, contact, email, age, sex, blood group, emergency contact, and photo.

## Forms

The forms are defined in [forms.py](http://_vscodecontentref_/24):

- [RegistrationForm](http://_vscodecontentref_/25): A form for registering patients.
- [ClinicForm](http://_vscodecontentref_/26): A form for adding clinics.

## Routes

The application routes are defined in [app.py](http://_vscodecontentref_/27):

- `/`: The home page.
- `/clinics`: Displays a list of clinics.
- `/add_clinic`: A form to add a new clinic.
- `/clinic/<int:clinic_id>`: Displays the home page for a specific clinic.
- `/clinic/<int:clinic_id>/register`: A form to register a new patient for a specific clinic.
- `/doctor_home`: The doctor's dashboard.
- `/patients`: Displays a list of patients.
- `/patient/<int:patient_id>`: Displays the details of a specific patient.
- `/patient/<int:patient_id>/modify`: A form to modify the details of a specific patient.
- `/patient/<int:patient_id>/delete`: Deletes a specific patient.

## Templates

The HTML templates are located in the [templates](http://_vscodecontentref_/28) directory:

- [add_clinic.html](http://_vscodecontentref_/29): Template for adding a new clinic.
- [clinic_home.html](http://_vscodecontentref_/30): Template for the clinic home page.
- [clinics.html](http://_vscodecontentref_/31): Template for displaying a list of clinics.
- [doctor_home.html](http://_vscodecontentref_/32): Template for the doctor's dashboard.
- [index.html](http://_vscodecontentref_/33): Template for the home page.
- [modify_patient.html](http://_vscodecontentref_/34): Template for modifying patient details.
- [patient_detail.html](http://_vscodecontentref_/35): Template for displaying patient details.
- [patients.html](http://_vscodecontentref_/36): Template for displaying a list of patients.
- [registration.html](http://_vscodecontentref_/37): Template for registering a new patient.

## Static Files

The static files (CSS, images, etc.) are located in the [static](http://_vscodecontentref_/38) directory:

- [styles.css](http://_vscodecontentref_/39): The main stylesheet for the application.
- `uploads/`: Directory for uploaded files (e.g., patient photos).

## License

This project is licensed under the MIT License.