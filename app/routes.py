import LoginForm as LoginForm
from flask import url_for, flash, render_template
from werkzeug.utils import redirect

from app import app
from app.models import Student, Parent, Teacher
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/index')
def index():
    return "hello world"


@app.route('/login', methods=['GET', 'POST'])
def login():
    global account
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        acc_type = form.username.data[0]
        index = form.username.data[1:]

        if acc_type == 'u':
            account = Student.query.filter_by(student_id=index).first()
            if account is None or not account.check_password(form.password.data):
                flash('Niepoprawny login lub hasło')
                return redirect(url_for('login'))

        elif acc_type == 'r':
            account = Parent.query.filter_by(parent_id=index).first()
            if account is None or not account.check_password(form.password.data):
                flash('Niepoprawny login lub hasło')
                return redirect(url_for('login'))

        elif acc_type == 'n':
            account = Teacher.query.filter_by(teacher_id=index).first()
            if account is None or not account.check_password(form.password.data):
                flash('Niepoprawny login lub hasło')
                return redirect(url_for('login'))

        login_user(account)

        return redirect(url_for('index'))
    return render_template('login.html', title="Logowanie", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(index))


@app.route('/user/profile')
@login_required
def profile(login):
    account = None
    if current_user.login[0] == 'u':
        account = Student.query.filter_by(student_id=current_user.student_id).first_or_404()
    elif current_user.login[0] == 'r':
        account = Parent.query.filter_by(parent_id=current_user.parent_id).first_or_404()
    elif current_user.login[0] == 'n':
        account = Teacher.query.filter_by(teacher_id=current_user.teacher_id).first_or_404()

    return render_template('user.html')