# Odontograma

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A django-based odontogram form. The odontogram scheme identify teeth with numbers and helps dentists to keep record on the patients dental treatments.

The motivation of this project was to integrate an odontogram  into another django app that keeps record of a dental office (patient appointments, payments, personal information, etc.).

## Project content

The odontogram allows to record different states of the teeth from a given patient in specifi tooth parts (lingual, distal, occlusal, bucal, mesial). These states include:

* Healthy tooth
* Cavities
* Restoration
* Extraction
* Erosion
* Dental plaque
* Inplant

The app was built in Spanish since this project is proposed to someone Hispanophone.

## Test the app

![](https://github.com/AaronMillOro/odontogram_form/blob/master/demo.gif)

1. Install and run pipenv to generate a virtual environment.

		pipenv install
        pipenv shell

2. Download the corresponding dependencies in the virtual environment.

		pip install -r requirements.txt

3. Run the application.

		python3 manage.py runserver 0.0.0.0:5000

4. Open your favorite web browser and type:

		http://localhost:5000/

Enjoy! :shipit: