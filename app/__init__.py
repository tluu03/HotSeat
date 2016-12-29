# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configs
app.config.from_object('config')

# Def db obj which is imported by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import module/ component using its blueprint handler variable (authorization)
from app.authentication.controllers import mod_auth as auth_module

# Register blueprints
app.register_blueprint(auth_module)

# Build db:
db.create_all()
