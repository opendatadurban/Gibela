from sqlalchemy.dialects.postgresql import JSON
from ..app import db
from ..forms import Form
from wtforms import StringField, IntegerField, FloatField, BooleanField, DateField
from wtforms_components import TimeField
from wtforms.validators import DataRequired, Length


class Rider(db.Model):
    __tablename__ = 'riders'

    id = db.Column(db.Integer, primary_key=True)
    pass_no = db.Column(db.Integer)
    lat_A = db.Column(db.Float)
    lon_A = db.Column(db.Float)
    lat_B = db.Column(db.Float)
    lon_B = db.Column(db.Float)
    w3w_A = db.Column(JSON)
    w3w_B = db.Column(JSON)
    monday = db.Column(db.Boolean)
    tuesday = db.Column(db.Boolean)
    wednesday = db.Column(db.Boolean)
    thursday = db.Column(db.Boolean)
    friday = db.Column(db.Boolean)
    saturday = db.Column(db.Boolean)
    sunday = db.Column(db.Boolean)
    once_off = db.Column(db.Boolean)
    rep_weekly = db.Column(db.Boolean)
    rep_biweekly = db.Column(db.Boolean)
    rep_monthly = db.Column(db.Boolean)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    departure_1 = db.Column(db.Time)
    departure_2 = db.Column(db.Time)
    arrival_1 = db.Column(db.Time)
    arrival_2 = db.Column(db.Time)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<id {}>'.format(self.id)


class RequestForm(Form):
    pass_no = IntegerField('Passenger Number', validators=[DataRequired()])
    lat_A = FloatField('Lat A', validators=[DataRequired()])
    lon_A = FloatField('Lon A', validators=[DataRequired()])
    lat_B = FloatField('Lat B', validators=[DataRequired()])
    lon_B = FloatField('Lon B', validators=[DataRequired()])
    w3w_A1 = StringField('W3WA1', validators=[DataRequired()])
    w3w_A2 = StringField('W3WA2', validators=[DataRequired()])
    w3w_A3 = StringField('W3WA3', validators=[DataRequired()])
    w3w_B1 = StringField('W3WB1', validators=[DataRequired()])
    w3w_B2 = StringField('W3WB2', validators=[DataRequired()])
    w3w_B3 = StringField('W3WB3', validators=[DataRequired()])
    monday = BooleanField('Monday')
    tuesday = BooleanField('Tuesday')
    wednesday = BooleanField('Wednesday')
    thursday = BooleanField('Thursday')
    friday = BooleanField('Friday')
    saturday = BooleanField('Saturday')
    Sunday = BooleanField('Sunday')
    once_off = BooleanField('Once-off')
    rep_weekly = BooleanField('Weekly')
    rep_biweekly = BooleanField('Bi-weekly')
    rep_monthly = BooleanField('Monthly')
    start_date = DateField('Start', validators=[DataRequired()])
    end_date = DateField('End', validators=[DataRequired()])
    departure_1 = TimeField('Departure 1', validators=[DataRequired()])
    departure_2 = TimeField('Departure 2', validators=[DataRequired()])
    arrival_1 = TimeField('Arrival 1', validators=[DataRequired()])
    arrival_2 = TimeField('Arrival 2', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
