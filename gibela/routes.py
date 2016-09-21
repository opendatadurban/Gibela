from gibela.app import app
from flask import request, url_for, flash, redirect
from flask_mako import render_template
from flask_security import current_user
from sqlalchemy.sql import func

from gibela.models import db, Rider, Provider
import gibela.riders
import gibela.providers


@app.route('/')
def home():
    if current_user.is_authenticated():
        if current_user.has_role('provider'):
            return redirect(url_for('provider_dashboard'))

        if current_user.has_role('rider'):
            return redirect(url_for('rider_dashboard'))

        return render_template('noperms.haml')
    else:
        return redirect(url_for('security.login'))
