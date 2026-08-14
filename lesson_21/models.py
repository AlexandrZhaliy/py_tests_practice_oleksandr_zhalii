# this module describes tables structure in which the data will be added
# tables creation will be executed within db_tables_creation.py module
# data filling will be executed within db_data_filling.py module

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

student_courses = Table(
    "student_courses",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True)
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String)
    courses = relationship(
        "Course",
        secondary=student_courses,
        back_populates="students"
    )

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    students = relationship(
        "Student",
        secondary=student_courses,
        back_populates="courses"
    )


