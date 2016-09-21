import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_ENABLED = True
SECRET_KEY = 'uhrmaHghurds3craTC0de!'
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/gibela'
