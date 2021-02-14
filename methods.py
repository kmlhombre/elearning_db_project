from models import Student, Teacher, Parent, Grade, Subject, Class
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:password@127.0.0.1:5432/elearningDB", echo=True)
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
    password_to_check = l.getPassword()
    if check_password_hash(password_to_check, password):
        return l, logged_status
    else:
        return None, None


def display_grades(login, logged_type):
    if logged_type == 'Parent':
        l = session.query(Parent).filter_by(login=login).first()
        id_student = l.student_id
    elif logged_type == 'Student':
        l = session.query(Student).filter_by(login=login).first()
        id_student = l.getId()

    return session.query(Grade, Subject).join(Subject).join(Student).filter_by(student_id=id_student).all()


def change_password(logged_user, password):
    new_password = generate_password_hash(password)
    login = logged_user

    l = session.query(Student).filter_by(login=login).first()
    if l is None:
        l = session.query(Teacher).filter_by(login=login).first()
        if l is None:
            l = session.query(Parent).filter_by(login=login).first()

    l.password = new_password
    session.commit()


def add_grade(student_id, subject_id, value):
    id_grade = max_grade_id().one().max_id
    val = int(value)
    grade = Grade(grade_id=id_grade+1, student_id=student_id, subject_id=subject_id, value=float(val))
    session.add(grade)
    session.commit()
    return True


def max_grade_id():
    return session.query(func.max(Grade.grade_id).label("max_id"))


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


def get_subjects():
    return session.query(Subject, Class).join(Class).all()


def get_students(subject, _class):
    _class_id = session.query(Class).filter(Class.name ==_class).first()
    sub = session.query(Subject).filter(Subject.name == subject, Subject.class_id == _class_id.class_id).first()
    #return session.query(Student, Grade).join(Class).join(Subject).join(Grade).filter(Subject.subject_id == sub.subject_id, Subject.class_id == _class_id.class_id).group_by(Grade.grade_id).all()
    return session.query(Student).select_from(Student).join(Class).join(Subject).filter(Subject.subject_id == sub.subject_id, Subject.class_id == _class_id.class_id).all()


def get_grades_of_student(subject, student_id):
    return session.query(Grade).distinct(Grade.grade_id).join(Subject).join(Class).join(Student).filter(Grade.student_id == student_id, Subject.subject_id == subject).all()


def get_subject_id(subject, c):
    _class_id = session.query(Class).filter(Class.name == c).first()
    return session.query(Subject).filter(Subject.name == subject, Subject.class_id == _class_id.class_id).first()