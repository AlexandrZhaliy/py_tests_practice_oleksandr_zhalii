# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def change_average_score(self, new_score):
        self.average_score = new_score
        return f"Name = {self.name}, Surname = {self.surname}, Age = {self.age}, Score = {self.average_score}"

student_01 = Student("Vasya", "Testerenko", 25, 10)

print(student_01.change_average_score(143))