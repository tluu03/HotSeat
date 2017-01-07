from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.student.forms import ManageStudentsForm
from app.student.services import StudentService as student_service

mod_student = Blueprint('students', __name__, url_prefix='/students')

@mod_student.route('/manage/', methods=['GET', 'POST'])
def manage():
    pass
