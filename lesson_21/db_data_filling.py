# this module adds data to already created tables in database
# before this module running, tables creation should be executed within db_tables_creation.py module

import random
from faker import Faker
from db_connect import session
from models import Student, Course


fake = Faker()

courses = [
    Course(name="Python", description="Python programming"),
    Course(name="SQL", description="Databases and SQL"),
    Course(name="Playwright", description="Web automation"),
    Course(name="API Testing", description="API testing"),
    Course(name="Git", description="Version control"),
]

session.add_all(courses)

for i in range(20):
    student = Student(
        name=fake.name(),
        age=random.randint(18, 40),
        email=fake.email(),
    )
    student.courses = random.sample(courses, random.randint(1, 3))
    session.add(student)

session.commit()
print("Database filled successfully!")