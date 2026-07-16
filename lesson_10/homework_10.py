# ====================== task 1 ===========================
# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
# які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім('я, зарплата, відділ), а також атрибут team_size,'
#                                                        'який вказує на кількість розробників у команді, якою керує керівник.)
#
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
from abc import abstractmethod


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

# test_01
# AQA_lead = TeamLead("Vasya", 4500, "AQA", "Haskell", 4)
# test_result = AQA_lead.name, AQA_lead.salary, AQA_lead.department, AQA_lead.programming_language
# print(test_result)

# test_02
# FE_lead = TeamLead("Petya", 5000, "Development dpt", "ReactJS", 6)
# assert hasattr(FE_lead, "name")
# assert hasattr(FE_lead, "salary")
# assert hasattr(FE_lead, "department")
# assert hasattr(FE_lead, "programming_language")
# print("Tests are passed")

# test_03
# import unittest
#
# class TestBELead(unittest.TestCase):
#     def test_attributes(self):
#         BE_lead = TeamLead("Kolya", 5500, "Development dpt", "NestJS", 7)
#
#         self.assertTrue(hasattr(BE_lead, "name"))
#         self.assertTrue(hasattr(BE_lead, "salary"))
#         self.assertTrue(hasattr(BE_lead, "department"))
#         self.assertTrue(hasattr(BE_lead, "programming_language"))
# if __name__ == "__main__":
#     unittest.main()

# ====================================================================================================================

# ====================== task 2 ===========================
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def area(self):
        p = (self.__side_a + self.__side_b + self.__side_c) / 2
        return math.sqrt(p*(p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c))

    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


figures = [
    Rectangle(5, 7),
    Triangle(6,4,8),
    Circle(3)
]

for entity in figures:
    print(
        f"{entity.__class__.__name__}: "
        f"Area = {entity.area()}, "
        f"Perimeter = {entity.perimeter():}"
    )