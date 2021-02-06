from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Class(db.Model):
    __tablename__ = 'Class'

    class_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Class {} {}>".format(self.name, self.year)


class Student(UserMixin, db.Model):
    __tablename__ = 'Student'

    student_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('Class.class_id'))
    first_name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    mail = db.Column(db.String(80), nullable=False, unique=True)
    login = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return "<Student {} {} {} {} {} {}>".format(self.first_name, self.surname, self.mail, self.login, self.password, self.birth_date)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_student(id):
    return Student.query.get(id)


class Parent(UserMixin, db.Model):
    __tablename__ = 'Parent'
    parent_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return "<Parent {} {} {} {}>".format(self.login, self.password, self.first_name, self.surname)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_parent(id):
    return Parent.query.get(id)


class Subject(db.Model):
    __tablename__ = 'Subject'
    subject_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('Class.class_id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('Teacher.teacher_id'))
    name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return "<Subject {} {} {} {}>".format(self.subject_id, self.class_id, self.teacher_id, self.name)


class Teacher(db.Model):
    __tablename__ = 'Teacher'

    teacher_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    mail = db.Column(db.String(80), nullable=False)
    login = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return "<Teacher {} {} {} {} {} {}>".format(self.first_name, self.surname, self.mail, self.login, self.password, self.birth_date)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Grade(db.Model):
    __tablename__ = 'Grade'

    grade_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('Student.student_id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('Subject.subject_id'))
    value = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return "<Grade {}>".format(self.value)
