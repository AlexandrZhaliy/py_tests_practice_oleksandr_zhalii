# task 01 == Виправте синтаксичні помилки
print("Task 01")

print("Hello", end = " ")
print("world!")

# ===========================================================================================================

# task 02 == Виправте синтаксичні помилки
print("Task 02")

hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# ===========================================================================================================

# task 03  == Вcтавте пропущену змінну у ф-цію print
print("Task 03")

for letter in "Hello world!":
    print(letter)

# ===========================================================================================================

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
# print("Task 04")
# print(banana) #added for check, commented as banana's displaying is not specified in the task



# ===========================================================================================================

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# ===========================================================================================================

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
print("Task 06")

perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)

# ===========================================================================================================

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
print()
print("Task 07")
# =================given===========================
#     ====intervals========
first_interval = 5
second_interval = 2

#     ====conditions=======
apples = 4
pears = apples + first_interval
plums = apples - second_interval

# ============item solutions=======================
print("Apples:", apples)
print("Pears:", apples, "+", first_interval, "=", pears)
print("Plums:", apples, "-", second_interval, "=", plums)

# ============general solution=====================
print("Total trees is the garden:", apples, "+", pears, "+", plums, "=", apples + pears + plums)

# ===========================================================================================================

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print()
print("Task 08")
# =================given===========================

#     ====intervals=====
first_interval = 5
second_interval = 10
third_interval = 4

#     ====conditions====
before_dinner = 0 + first_interval
after_dinner = before_dinner - second_interval
evening = after_dinner + third_interval

# ============time-slots solutions=======================
print("Before dinner:", 0, "+", first_interval, "=", before_dinner)
print("After dinner:", before_dinner, "-", second_interval, "=", after_dinner)
print("Evening:", after_dinner, "+", third_interval, "=", evening)

# ============general solution=====================
print("Evening temperature is:", evening)

# ===========================================================================================================

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print()
print("Task 09")
# =================given===========================

#     ====class-register====
boys_total = 24
girls_total = int(boys_total / 2)
pupils_total = boys_total + girls_total

'''
girls_total divider is hardcoded comparing with the previous tasks as not pupils-quantity but
their presence is the main task-subject. So class-roster can be taken as a constant
'''

#     ====absences=====
boys_absent = 1
girls_absent = 2

#     ====presences=====
boys_present = boys_total - boys_absent
girls_present = girls_total - girls_absent
pupils_present = boys_present + girls_present

# ============class-register-display=======================
print("Boys total:", boys_total)
print("Girls total:", girls_total)

# ============pupils present=======================
print("Boys present:", boys_total, "-", boys_absent, "=", boys_present)
print("Girls present:", girls_total, "-", girls_absent, "=", girls_present)

# ============general solution=====================
print("Total pupils are present:", boys_present, "+", girls_present, "=", pupils_present)

# ===========================================================================================================

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

print()
print("Task 10")
# =================given===========================

#     ====price-steps====
step_1 = 2
step_2 = 2
#     ====book-prices=====
currency = "UAH"
first_book = 8
second_book = first_book - step_1
third_book = int((first_book + second_book) / step_2)

# ============prices-roster=======================
print("The First Book:", first_book, currency)
print("The Second Book:", first_book, "-", step_1, "=", second_book, currency)
print("The Third Book:", "(", first_book, "+", second_book, ")", "/", step_2, "=", third_book, currency)

# ============total-amount=======================
print("Total books amount is:", first_book, "+", second_book, "+", third_book, "=", first_book + second_book + third_book, currency)