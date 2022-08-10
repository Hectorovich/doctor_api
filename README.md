### Doctor API


### [Task](https://docs.google.com/document/d/1u2wLu1Xzv67xUO_ccAknfbY03BG1CxUiWu39Y4EIGbg/edit#)

### Installation

Python3 must be already installed
````
git clone https://github.com/Hectorovich/doctor_api
cd doctor_api
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
python manage.py runserver
````

### Endpoints
* To get list of endpoints: GET /api/doctor/
* To get list of doctors: GET /api/doctor/doctors/
* To create new doctor: POST /api/doctor/doctors/
* To get list of specializations: GET /api/doctor/specializations/
* To create new specialization: POST /api/doctor/specializations/
