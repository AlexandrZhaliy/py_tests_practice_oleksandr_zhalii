from db_connect import session
from models import Student, Course


# ========== Students registered for a specific course =================
course = session.query(Course).filter_by(name="Python").first()
print(f"Students registered for {course.name}:")
for student in course.students:
    print(student.name)

# ========== Courses registered for a specific student =================
student = session.query(Student).filter_by(name="Vasya Testerenko").first()
print(f"\nCourses registered for {student.name}:")
for course in student.courses:
    print(course.name)