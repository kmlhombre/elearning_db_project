from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug import check_password_hash, generate_password_hash
from models import Student, Parent, Teacher


engine = create_engine("sqlite:///test.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def mass_change_of_passwords():
    students = session.query(Student).all()
    for student in students:
        student.password = generate_password_hash(student.password)

    parents = session.query(Parent).all()
    for parent in parents:
        parent.password = generate_password_hash(parent.password)

    teachers = session.query(Teacher).all()
    for teacher in teachers:
        teacher.password = generate_password_hash(teacher.password)

    session.commit()
