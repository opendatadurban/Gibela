import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'uhrmaHghurds3craTC0de!'
    SQLALCHEMY_DATABASE_URI = os.environ['postgresql://localhost/gibela']
