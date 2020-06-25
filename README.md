# python-flask-api
This is a repository for flask restful api code, for an user content administration dashboard

### Dependencies
* Built with Python 3.8

## Setup
* Create python virtual environment ```$ virtualenv venv```
* Install all requirementes from `requirementes.txt` with ```$ pip install -r requirements.txt```
* Generate database with the following commands
  * ```$ python manage.py db init```
  * ```$ python manage.py db python manage.py db migrate```
  * ```$ python manage.py db upgrade```
* Run the application with ```$ python manage.py run```
