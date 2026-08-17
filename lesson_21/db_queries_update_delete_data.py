from db_connect import session
from models import Student, Course

# =========== Specific student data changing =============
# student = session.query(Student).filter_by(
#     email="vasya_testerenko@service.domain"
# ).first()
#
# if student is None:
#     print("Student not found")
# else:
#     # student.name = "Petya KYA"
#     student.age = 31
#     # student.email = "petya_kya@service.domain"
#     session.commit()
#     print(f"Student {student.name} updated successfully!")

# =========== Specific course data changing =============
course = session.query(Course).filter_by(
    name="Python"
).first()

if course is None:
    print("Course not found")
else:
    # course.name = "Python Note Pro Max+ 5G 128GB"
    course.description = "Advanced Python programming"
    session.commit()
    print(f"Course {course.name} updated successfully!")

# =========== Specific student deleting from db =============
# student = session.query(Student).filter_by(
#     email="petya_kya@service.domain"
# ).first()
#
# if student is None:
#     print("Student not found")
# else:
#     session.delete(student)
#     session.commit()
#     print(f"Student {student.name} deleted successfully!")