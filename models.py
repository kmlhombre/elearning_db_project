from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Class(Base):
    __tablename__ = 'Class'

    class_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    year = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Class {} {}>".format(self.name, self.year)


class Student(Base):
    __tablename__ = 'Student'

    student_id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey('Class.class_id'))
    first_name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    mail = Column(String(80), nullable=False)
    login = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    birth_date = Column(Date, nullable=False)

    def getPassword(self):
        return self.password

    def getLogin(self):
        return self.login

    def getId(self):
        return self.student_id

    def __repr__(self):
        return "<Student {} {} {} {} {} {}>".format(self.first_name, self.surname, self.mail, self.login, self.password, self.birth_date)


class Parent(Base):
    __tablename__ = 'Parent'

    parent_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('Student.student_id'))
    login = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    first_name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)

    def __repr__(self):
        return "<Parent {} {} {} {}>".format(self.login, self.password, self.first_name, self.surname)

    def getPassword(self):
        return self.password

    def getLogin(self):
        return self.login

    def getId(self):
        return self.student_id


class Teacher(Base):
    __tablename__ = 'Teacher'

    teacher_id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    mail = Column(String(80), nullable=False)
    login = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    birth_date = Column(Date, nullable=False)

    def __repr__(self):
        return "<Teacher {} {} {} {} {} {}>".format(self.first_name, self.surname, self.mail, self.login, self.password, self.birth_date)

    def getPassword(self):
        return self.password

    def getLogin(self):
        return self.login

    def getId(self):
        return self.teacher_id


class Grade(Base):
    __tablename__ = 'Grade'

    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('Student.student_id'))
    subject_id = Column(Integer, ForeignKey('Subject.subject_id'))
    value = Column(Integer, nullable=True)

    def __repr__(self):
        return "<Grade {}>".format(self.value)


class Subject(Base):
    __tablename__ = 'Subject'

    subject_id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey('Class.class_id'))
    teacher_id = Column(Integer, ForeignKey('Teacher.teacher_id'))
    name = Column(String(30), nullable=False)

    def __repr__(self):
        return "<Subject {} {} {} {}>".format(self.subject_id, self.class_id, self.teacher_id, self.name)
