from flask_wtf import Form
from wtforms import StringField, BooleanField, IntegerField, FormField
from wtforms.validators import DataRequired


class TelephoneForm(Form):
    area_code = IntegerField('Area Code', validators=[DataRequired()])
    number = StringField('Number')


class LoginForm(Form):
    user_id = StringField('User ID', validators=[DataRequired()])
    phone = FormField(TelephoneForm)
    remember_me = BooleanField('remember_me', default=False)
