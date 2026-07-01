# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
from lesson_01.homework_01_Oleksandr_Zhalii import storona_1


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 25:
        result = number * multiplier
        # десь тут помил%к%а, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# student's note: for multiplier == 3 and max.result == 25, the following output rows should appear as well:
# 3x6=18
# 3x7=21
# 3x8=24

# =================================================================================================================

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def two_numbers_sum(a, b):
    summary = a + b
    return summary
# test_01
# print(two_numbers_sum(2, 2))

# =================================================================================================================

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_average(*numbers):
    dividend = sum(numbers)
    divisor = len(numbers)
    if divisor == 0:
        return "Enter at least one argument"
    return dividend/divisor

# test_02
# print(arithmetic_average(2,43,654,53,1,0,5))
# test_03
# print(arithmetic_average())

# =================================================================================================================

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def string_reverse(task4_string):
    return task4_string[::-1]

# test_04
# print(string_reverse(input()))

# =================================================================================================================

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

# ======================= variant for list =====================================
def longest_word_1(task5_1_input):
    return max(task5_1_input, key=len)

# test_05
# print(longest_word_1(task5_1_input=["one", "two", "three", "four", "five"]))

# =================== variant for anything entered =============================
def longest_word_2(task5_2_input):
    words = task5_2_input.split()
    return max(words, key=len)

# test_06
# print(longest_word_2(input()))

# =================================================================================================================

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

# ======================= easy solution ===============================
def find_substring(str1, str2):
        return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# =============== more practice, suggested solution (I guess) ===========
def find_substring(str1, str2):
    for index in range(len(str1)):
        if str1[index:index+len(str2)] == str2:
            return index
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# =================================================================================================================

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# =============== lesson_01, task 5, 6 ========================

def perimeter(*sides):
    """calculates any sided-figure perimeter bu accepting it's side-sizes"""
    return sum(sides)

print(perimeter(1, 2, 3, 4))

# =============== lesson_03, task 10 ========================
def fuel_required(trip_distance, consumption_distance, consumption_volume):
    """Calculates how much fuel required for defined distance trip according a car's consumption (litres per 100 km)"""
    """Result returned in full litres to cover 100% of path"""
    total_consumption = trip_distance / consumption_distance * consumption_volume
    return int(total_consumption +1)

def tanks_required(fuel_required, tank_volume):
    """Calculates how much tank-fillings required for defined distance, consumption l/km and tank volume"""
    """Result returned in full tanks to cover 100% of path"""
    """Warning! Calculation does not apply to the remaining fuel reserve."""
    return fuel_required/tank_volume

print(fuel_required(1599, 100, 9))
print(tanks_required(fuel_required(1599, 100, 9), 48))

# =============== lesson_03, task 8 ========================
def order_price_calculator(items):
    """This function calculates total order amount for list of tuples with items, quantity and price"""
    total = 0
    for name, quantity, price in items:
        total += price * quantity
    return total

items = [
    ("Піца велика", 4, 274),
    ("Піца середня", 2, 218),
    ("Сік", 4, 35),
    ("Торт", 1, 350),
    ("Вода", 3, 21)
]

print(order_price_calculator(items))

# =============== lesson_06, task 4 ========================
def even_numbers_selector(*numbers):
    """This function extracts even-numbers from any entered number sequence"""
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

print(even_numbers_selector(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 155, 3571, 94586))