# Import Form
from flask.ext.wtf import Form #o

# Import Form elements such as TextField and BooleanField
from wtforms import TextField, PasswordField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo

# Define login from WTForms

class LoginForm(Form):
    email = TextField('Email Address', [Email(), Required(message='Forgot your email?')])

    password = PasswordField('Password', [Required(message='Must provide a password.')])
