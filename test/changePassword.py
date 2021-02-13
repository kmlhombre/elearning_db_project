from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from models import Student, Parent, Teacher


engine = create_engine("postgresql://postgres:password@127.0.0.1:5432/elearningDB", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


"""def mass_change_of_passwords():
    students = session.query(Student).all()
    for student in students:
        temp = generate_password_hash(student.password)
        student.password = temp
        session.commit()

    parents = session.query(Parent).all()
    for parent in parents:
        temp = generate_password_hash(parent.password)
        parent.password = temp
        session.commit()

    teachers = session.query(Teacher).all()
    for teacher in teachers:
        temp = generate_password_hash(teacher.password)
        teacher.password = temp
        session.commit()"""

student = session.query(Student).first()
print(type(student.password), len(student.password))
passwd = "s10001ms"
if check_password_hash(student.password, passwd):
    print("OK")
else:
    print("NOT OK")