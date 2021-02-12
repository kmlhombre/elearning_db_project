from models import Student, Teacher, Parent, Grade, Subject, Class
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///test.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def login_user(login, password):
    l = session.query(Student).filter_by(login=login).first()
    logged_status = "Student"
    if l is None:
        l = session.query(Teacher).filter_by(login=login).first()
        logged_status = "Teacher"
        if l is None:
            l = session.query(Parent).filter_by(login=login).first()
            logged_status = "Parent"
            if l is None:
                return None, None

    password = generate_password_hash(password)
    password_to_check = l.getPassword()

    if check_password_hash(password_to_check, password):
        return l, logged_status
    else:
        return None, None


def logout(logged_user):
    logged_user = None


def display_grades(login, subject):
    l = session.query(Student).filter_by(login=login).first()
    if l is None:
        l = session.query(Teacher).filter_by(login=login).first()
    id = l.getId()

    return session.query(Grade).join(Subject).filter_by(student_id=id, name=subject).all()


def change_password(logged_user, password):
    new_password = generate_password_hash(password)
    login = logged_user.getLogin()

    l = session.query(Student).filter_by(login=login).first()
    if l is None:
        l = session.query(Teacher).filter_by(login=login).first()
        if l is None:
            l = session.query(Parent).filter_by(login=login).first()

    l.password = new_password
    session.commit()


def add_grade(logged_user):
    subjects = session.query(Subject).filter_by(teacher_id=logged_user.getId()).all()
    if len(subjects) == 0:
        return "Blad systemu"

    sub_id = subject_menu(subjects)
    classes = session.query(Subject).join(Class).filter_by(subject_id=sub_id).all()
    class_id = classes_menu(classes)
    students = session.query(Student).filter_by(class_id=class_id).all()
    student_id = student_menu(students)
    max_id_grade = session.query(func.max(Grade.grade_id))

    print("Wpisz ocene: ")

    value = 0
    while value < 1 or value > 6:
        value = int(input())

    grade = Grade(grade_id=max_id_grade+1, student_id=student_id, subject_id=sub_id, value=value)
    session.add(grade)
    session.commit()


def edit_grade(logged_user):
    subjects = session.query(Subject).filter_by(teacher_id=logged_user.getId()).all()
    if len(subjects) == 0:
        return "Blad systemu"

    sub_id = subject_menu(subjects)
    classes = session.query(Subject).join(Class).filter_by(subject_id=sub_id).all()
    class_id = classes_menu(classes)
    students = session.query(Student).filter_by(class_id=class_id).all()
    student_id = student_menu(students)
    grades = session.query(Grade).filter_by(student_id=student_id, subject_id=sub_id).all()
    grade_id = grade_menu(grades)
    grade = session.query(Grade).filter_by(grade_id=grade_id).first()

    print("Edytuj ocene: ")

    value = 0
    while value < 1 or value > 6:
        value = int(input())

    grade.value = value
    session.commit()

    
def subject_menu(subjects):
    while True:
        print("Wybierz przedmiot: ")

        subject_id_list = []
        subject_id_list.clear()

        for subject in subjects:
            print(subject.subject_id, ". ", subject.name)
            subject_id_list.append(subject.subject_id)

        subject_id = int(input())
        if subject_id in subject_id_list:
            return subject_id


def classes_menu(classes):
    while True:
        print("Wybierz klase: ")
        classes_id_list = []
        classes_id_list.clear()

        for s, c in classes:
            print(c.class_id, ". ", c.name)
            classes_id_list.append(c.class_id)

        class_id = int(input())
        if class_id in classes_id_list:
            return class_id


def student_menu(students):
    while True:
        print("Wybierz ucznia: ")
        student_id_list = []
        student_id_list.clear()

        for student in students:
            print(student.student_id, ". ", student.surname, " ", student.first_name)
            student_id_list.append(student.student_id)

        student_id = int(input())
        if student_id in student_id_list:
            return student_id


def grade_menu(grades):
    while True:
        print("Wybierz ocene: ")
        grade_id_list = []
        grade_id_list.clear()

        for grade in grades:
            print(grade.grade_id, ". ", grade.value)
            grade_id_list.append(grade.student_id)

        grade_id = int(input())
        if grade_id in grade_id_list:
            return grade_id


def display_classes_grades(logged_user):
    subjects = session.query(Subject).filter_by(teacher_id=logged_user.getId()).all()
    if len(subjects) == 0:
        return "Blad systemu"

    sub_id = subject_menu(subjects)
    classes = session.query(Subject).join(Class).filter_by(subject_id=sub_id).all()
    class_id = classes_menu(classes)
    all_grades = session.query(Student).join(Grade).filter(Subject.subject_id == sub_id, Student.class_id == class_id).all()

    return all_grades


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


def get_subjects():
    return session.query(Subject).all()


def get_students(subject):
    sub = session.query(Subject).filter_by(name=subject).first()
    return session.query(Grade).join(Class).join(Subject).join(Student).filter(Subject.subject_id == sub.subject_id).all()

def get_grades_of_student(subject, student_id):
    return session.query(Grade).join(Class).join(Subject).join(Student).filter(Student.student_id == student_id, Subject.name == subject).all()