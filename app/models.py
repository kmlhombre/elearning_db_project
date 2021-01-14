from app import db


class Class(db.Model):
    __tablename__ = 'Class'

    class_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Class {} {}>".format(self.name, self.year)


class Student(db.Model):
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


class Parent(db.Model):
    __tablename__ = 'Parent'
    parent_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return "<Parent {} {} {} {}>".format(self.login, self.password, self.first_name, self.surname)


class Subject(db.Model):
    __tablename__ = 'Subject'
    subject_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('Class.class_id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('Teacher.teacher_id'))
    name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return "<Subject {} {} {} {}>".format(self.subject_id, self.class_id, self.teacher_id, self.name)
