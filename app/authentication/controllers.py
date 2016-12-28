# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# Import pw/ encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import db obj from main app module
from app import db

# Import module forms
from app.authentication.forms import LoginForm

# Import module models
from app.authentication.models import User

# Define blueprint: 'auth', set its url prefix: app.url/auth
mod_auth  = Blueprint('auth', __name__, url_prefix='/auth')

# Set route and accepted methods
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)

    if (form.validate_on_submit()):
        user = User.query.filter_by(email=form.email.data).first()

        if (user and check_password_hash(user.password, form.password.data)):
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)

            return redirect(url_for('auth.home'))

        flash('Wrong email/ password', 'error-message')

    return render_template("authentication/signin.html", form=form)
