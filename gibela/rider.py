from gibela.app import app
from flask_mako import render_template
from flask_security import roles_accepted, current_user, login_required
from sqlalchemy.orm import joinedload

from .models import db, Rider, Provider
from .models.riders import RequestForm


@app.route('/rider')
@login_required
@roles_accepted('rider')
def rider_dashboard():
    # form = RequestForm()

    return render_template('rider/rider_dashboard.haml')

@app.route('/new_ride')
@login_required
@roles_accepted('rider')
def new_ride():
    form = RequestForm()
    return render_template('rider/new_ride.haml', form=form)
