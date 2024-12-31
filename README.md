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

- [User](http://_vscodecontentref_/22): Represents a user with fields for username, email, and password hash.
- [Clinic](http://_vscodecontentref_/23): Represents a clinic with fields for name, contact, owner, head doctor, address, and photo.
- [Patient](http://_vscodecontentref_/24): Represents a patient with fields for first name, last name, address, contact, email, age, sex, blood group, emergency contact, photo, and user_id.

## Forms

The forms are defined in [forms.py](http://_vscodecontentref_/25):

- [RegistrationForm](http://_vscodecontentref_/26): A form for registering patients.
- [ClinicForm](http://_vscodecontentref_/27): A form for adding clinics.
- [LoginForm](http://_vscodecontentref_/28): A form for user login.
- [RegisterForm](http://_vscodecontentref_/29): A form for user registration.

## Routes

The application routes are defined in [app.py](http://_vscodecontentref_/30):

- `/`: The home page.
- `/login`: A form for user login.
- `/register`: A form for user registration.
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

The HTML templates are located in the [templates](http://_vscodecontentref_/31) directory:

- [add_clinic.html](http://_vscodecontentref_/32): Template for adding a new clinic.
- [clinic_home.html](http://_vscodecontentref_/33): Template for the clinic home page.
- [clinics.html](http://_vscodecontentref_/34): Template for displaying a list of clinics.
- [doctor_home.html](http://_vscodecontentref_/35): Template for the doctor's dashboard.
- [index.html](http://_vscodecontentref_/36): Template for the home page.
- [login.html](http://_vscodecontentref_/37): Template for user login.
- [modify_patient.html](http://_vscodecontentref_/38): Template for modifying patient details.
- [patient_detail.html](http://_vscodecontentref_/39): Template for displaying patient details.
- [patients.html](http://_vscodecontentref_/40): Template for displaying a list of patients.
- [register_user.html](http://_vscodecontentref_/41): Template for user registration.
- [registration.html](http://_vscodecontentref_/42): Template for registering a new patient.

## Static Files

The static files (CSS, images, etc.) are located in the [static](http://_vscodecontentref_/43) directory:

- [styles.css](http://_vscodecontentref_/44): The main stylesheet for the application.
- `uploads/`: Directory for uploaded files (e.g., patient photos).

## Running on a VPS

To run this application on a VPS, follow these steps:

1. **Install PostgreSQL**:
    ```sh
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    ```

2. **Create a PostgreSQL Database and User**:
    ```sh
    sudo -i -u postgres
    psql
    CREATE DATABASE medical_clinic;
    CREATE USER clinic_user WITH PASSWORD 'your_password';
    ALTER ROLE clinic_user SET client_encoding TO 'utf8';
    ALTER ROLE clinic_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE clinic_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE medical_clinic TO clinic_user;
    \q
    exit
    ```

3. **Update the Configuration**:
    Update the `DATABASE_URL` environment variable in your VPS to point to the PostgreSQL database:
    ```sh
    export DATABASE_URL="postgresql://clinic_user:your_password@localhost/medical_clinic"
    ```

4. **Install Gunicorn**:
    ```sh
    pip install gunicorn
    ```

5. **Run the Application with Gunicorn**:
    ```sh
    gunicorn -w 4 -b 0.0.0.0:80 app:app
    ```

## License

This project is licensed under the MIT License.
