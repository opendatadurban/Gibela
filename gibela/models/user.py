from ..app import db, app
from flask_mako import render_template

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship
from flask_security import UserMixin, RoleMixin, Security, SQLAlchemyUserDatastore
from flask_security.forms import LoginForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length, InputRequired

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE')))


class User(db.Model, UserMixin):
    """
    A user who can login and use Gibela.
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    disabled = db.Column(db.Boolean(), default=False)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def full_name(self):
        s = '%s %s' % (self.first_name or '', self.last_name or '')
        s = s.strip()

        if not s:
            s = self.username

        return s

    def __repr__(self):
        return "<User email=%s>" % (self.username,)

    # Flask-Security requires an active attribute
    @property
    def active(self):
        return not self.disabled

    @active.setter
    def active(self, value):
        self.disabled = not value

    @classmethod
    def create_defaults(self):
        from flask_security.utils import encrypt_password

        admin_user = User()
        admin_user.username = "gibela"
        admin_user.first_name = "Gibela"
        admin_user.last_name = "Tester"
        admin_user.password = encrypt_password('gibela')

        return [admin_user]


class Role(db.Model, RoleMixin):
    """
        A user who can login and use Gibela.
    """
    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __unicode__(self):
        return unicode(self.name)

    @classmethod
    def create_defaults(self):
        return [
            Role(name='rider', description='user can supply ride information and request rides in return'),
            Role(name='provider', description='user can bid for and provide services'),
        ]


class ExtendedLoginForm(LoginForm):
    email = StringField('Username', [InputRequired()])


# user authentication
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore,
                    login_form=ExtendedLoginForm)
app.extensions['security'].render_template = render_template




