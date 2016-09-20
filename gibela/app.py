from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# setup templates and haml
from flask.ext.mako import MakoTemplates, _lookup, render_template
import haml

MakoTemplates(app)
app.config['MAKO_PREPROCESSOR'] = haml.preprocessor
app.config['MAKO_TRANSLATE_EXCEPTIONS'] = False
app.config['MAKO_DEFAULT_FILTERS'] = ['decode.utf8']

# CSRF protection
from flask_wtf.csrf import CsrfProtect

CsrfProtect(app)

# Database
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Mail
from flask_mail import Mail

mail = Mail(app)

import gibela.routes
