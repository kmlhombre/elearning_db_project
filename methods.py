from models import Student, Teacher, Parent, Grade, Subject
from werkzeug.security import generate_password_hash, check_password_hash


def login(session):
    print("Login: ")
    login = input()
    print("Hasło: ")
    password = input()

    l = session.query(Student).filter_by(login=login).first()
    if l is None:
        l = session.query(Teacher).filter_by(login=login).first()
        if l is None:
            l = session.query(Parent).filter_by(login=login).first()
        else:
            return "Niepoprawny login lub hasło"

    password = generate_password_hash(password)
    password_to_check = l.getPassword()

    if password == check_password_hash(password_to_check):
        return l
    else:
        return "Niepoprawny login lub hasło"


def logout(logged_user):
    logged_user = None


def display_grades(session, logged_user):
    login = logged_user.getLogin()
    l = session.query(Student).filter_by(login=login).first()
    if l is None:
        l = session.query(Teacher).filter_by(login=login).first()
    id = l.getId()

    return session.query(Grade).join(Subject).filter_by(student_id=id)


def change_password(session, logged_user, password):
    new_password = generate_password_hash(password)
    login = logged_user.getLogin()

    l = session.query(Student).filter_by(login=login).first()
    if l is None:
        l = session.query(Teacher).filter_by(login=login).first()
        if l is None:
            l = session.query(Parent).filter_by(login=login).first()

    l.password = new_password
    session.commit()
