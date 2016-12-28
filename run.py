# Run test server.
from app import app

app.run(host='0.0.0.0', port=8080, debug=True)

'''
# This is from hotseat.py before modularization

from flask import flask, render_template
from flask_restful import reqparse, resource, api
import json

app = flask(__name__)
api = api(app)

parser = reqparse.requestparser()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_students')
def get_students():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=true)
'''
