from app import app, db
from models import Student, Major
import datetime as dt

with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of majors
    majors = ['Aerospace Engineering', 'Biology', 'Civil Engineering', 'Computer Science',
              'Electrical Engineering', 'Finance', 'Information Systems', 'Marketing',
              'Mechanical Engineering']
    for each_major in majors:
        print(each_major)
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()

    # Initial loading of students first_name, last_name, major_id, birth_date, is_honors
    students = [
        {'student_id': '1', 'first_name': 'Robert', 'last_name':'Smith', "email": "robert.smith@example.com", 'major_id':3,
            'birth_date': dt.datetime(2005, 6, 1), 'is_honors':1},
        {'student_id': '2', 'first_name': 'Leo', 'last_name': 'Van Munching', "email": "leo.vanmunching@example.com", 'major_id':6,
         'birth_date': dt.datetime(2004, 3, 24), 'is_honors': 0},
    ]

    for each_student in students:
        print(f'{each_student["first_name"]} {each_student["last_name"]} inserted into Student')
        a_student = Student(first_name=each_student["first_name"], last_name=each_student["last_name"],
                            major_id=each_student["major_id"], birth_date=each_student["birth_date"],
                            is_honors=each_student["is_honors"], email=each_student["email"])
        db.session.add(a_student)
        db.session.commit()


