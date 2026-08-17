from db_connect import session
from models import Student, Course


student = Student(
    name="Vasya Testerenko",
    age=30,
    email="vasya_testerenko@service.domain",
)

course = session.query(Course).filter_by(name="Python").first()
student.courses.append(course)
session.add(student)

session.commit()
print("Student created successfully!")