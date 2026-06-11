# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
from math import remainder

alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?" \n'
                       '"That depends a good deal on where you want to get to," said the Cat. \n'
                       '"I don\'t much care where —" said Alice. \n'
                       '"Then it doesn\'t matter which way you go," said the Cat. \n'
                       '"— so long as I get somewhere," Alice added as an explanation. \n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
                       )

another_alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don\'t much care where —— " said Alice.
"Then it doesn\'t matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."
'''

print("Tasks 1, 2, 3: \n"
      f"\t{alice_in_wonderland.replace('\n', '\n\t')}\n"
      "\n"
      f"\t{another_alice_in_wonderland.replace('\n', '\n\t')}"
      )

# ===========================================================================================================

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
# =================given===========================

#     ====seas squares====
black_sea = 436402
sea_of_azov = 37800
measurement = 'sq.km'

#     ====total square====
total_seas_square = black_sea + sea_of_azov

# ============given-displaying=======================
print(f"Task 4:\n"
      f"Black Sea: {black_sea} {measurement}\n"
      f"Sea of Azov: {sea_of_azov} {measurement}"
      )

# ============solution=======================
print(f"Total quare of the seas: {black_sea} + {sea_of_azov} = {total_seas_square} {measurement}"
      f"\n")

# ===========================================================================================================

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# =================given===========================

#     ====warehouses shared quantities====
first_with_second = 250449
second_with_third = 222950
total_items = 375291

#     ====warehouses separated quantities====
first_warehouse = total_items - second_with_third
second_warehouse = first_with_second - first_warehouse
third_warehouse = total_items - first_with_second

# ============given-displaying=======================
print(f"Task 5:\n"
      f"Total items of warehouses: {total_items}\n"
      f"Items on the first and the second warehouses: {first_with_second}\n"
      f"Items on the second and the third warehouses: {second_with_third}\n"
      )

# ============solution=======================
print(f"The First Warehouse: {total_items} - {second_with_third} = {first_warehouse}\n"
      f"The Second Warehouse: {first_with_second} - {first_warehouse} = {second_warehouse}\n"
      f"The Third Warehouse: {total_items} - {first_with_second} = {third_warehouse}"
      f"\n")

# ===========================================================================================================

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# =================given===========================
deposit_monthly = 1179
deposit_currency = "UAH"
deposit_period = 18
pc_price = deposit_monthly * deposit_period

# ============solution=======================
print(f"Task 6:\n"
      f"Monthly basis deposit is: {deposit_monthly} {deposit_currency}\n"
      f"Loan period is: {deposit_period}\n"
      f"Computer price is: {deposit_monthly} * {deposit_period} = {pc_price} {deposit_currency}"
      f"\n")

# ===========================================================================================================

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# =================given===========================
# a)
dividend_a = 8019
divisor_a = 8
quotient_a = dividend_a // divisor_a
remainder_a = dividend_a % divisor_a
truncated_dividend_a = quotient_a * divisor_a

# b)
dividend_b = 9907
divisor_b = 9
quotient_b = dividend_b // divisor_b
remainder_b = dividend_b % divisor_b
truncated_dividend_b = quotient_b * divisor_b

# c)
dividend_c = 2789
divisor_c = 5
quotient_c = dividend_c // divisor_c
remainder_c = dividend_c % divisor_c
truncated_dividend_c = quotient_c * divisor_c

# d)
dividend_d = 7248
divisor_d = 6
quotient_d = dividend_d // divisor_d
remainder_d = dividend_d % divisor_d
truncated_dividend_d = quotient_d * divisor_d

# e)
dividend_e = 7128
divisor_e = 5
quotient_e = dividend_e // divisor_e
remainder_e = dividend_e % divisor_e
truncated_dividend_e = quotient_e * divisor_e

# f)
dividend_f = 19224
divisor_f = 9
quotient_f = dividend_f // divisor_f
remainder_f = dividend_f % divisor_f
truncated_dividend_f = quotient_f * divisor_f

# ============solution=======================
print(f"Task 7:\n"
      f"a) 8019 : 8 = {dividend_a/divisor_a}; {quotient_a} * {divisor_a} = {truncated_dividend_a}; {dividend_a} - {truncated_dividend_a} = {remainder_a}\n"
      f"b) 9907 : 9 = {dividend_b/divisor_b}; {quotient_b} * {divisor_b} = {truncated_dividend_b}; {dividend_b} - {truncated_dividend_b} = {remainder_b}\n"
      f"c) 2789 : 5 = {dividend_c/divisor_c}; {quotient_c} * {divisor_c} = {truncated_dividend_c}; {dividend_c} - {truncated_dividend_c} = {remainder_c}\n"
      f"d) 7248 : 6 = {dividend_d/divisor_d}; {quotient_d} * {divisor_d} = {truncated_dividend_d}; {dividend_d} - {truncated_dividend_d} = {remainder_d}\n"
      f"e) 7128 : 5 = {dividend_e/divisor_e}; {quotient_e} * {divisor_e} = {truncated_dividend_e}; {dividend_e} - {truncated_dividend_e} = {remainder_e}\n"
      f"f) 19224 : 9 = {dividend_f/divisor_f}; {quotient_f} * {divisor_f} = {truncated_dividend_f}; {dividend_f} - {truncated_dividend_f} = {remainder_f}\n"
      )

# ===========================================================================================================

# task 07, framework_edition
# =================given===========================
tasks = [(8019, 8),
         (9907, 9),
         (2789, 5),
         (7248, 6),
         (7128, 5),
         (19224, 9)
         ]

# ==========math===============
def solve_division(dividend_math, divisor_math):
    quotient_math = dividend_math // divisor_math
    remainder_math = dividend_math % divisor_math
    truncated_dividend_math = quotient_math * divisor_math

    return {
        "dividend": dividend_math,
        "divisor": divisor_math,
        "quotient": quotient_math,
        "remainder": remainder_math,
        "truncated": truncated_dividend_math
    }

# ==========output==============
def output(solution):
    dividend_output = solution["dividend"]
    divisor_output = solution["divisor"]
    quotient_output = solution["quotient"]
    truncated_output = solution["truncated"]
    remainder_output = solution["remainder"]

    print(f"{literation} {dividend_output} : {divisor_output}\n"
          f"Quotient = {quotient_output}\n"
          f"{quotient_output} * {divisor_output} = {truncated_output}\n"
          f"{dividend_output} - {truncated_output} = {remainder_output}\n"
          f"Remainder = {remainder_output}\n"
          )

# ============solution=======================
print("Task 7, framework edition:\n")

for index, (dividend, divisor) in enumerate(tasks):
    literation = chr(ord("a") + index) + ")"
    solution = solve_division(dividend, divisor)
    output(solution)

# ===========================================================================================================

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
# =================given===========================
#     ====prices====
prices = {
    "pizza_big": 274,
    "pizza_medium": 218,
    "juice": 35,
    "cake": 350,
    "water": 21
    }
currency = "UAH"

#     ====quantity====
quantity = {
    "pizza_big": 4,
    "pizza_medium": 2,
    "juice": 4,
    "cake": 1,
    "water": 3
    }

#     ====total amounts====
item_totals = {}

for item in prices:
    item_totals[item] = prices[item] * quantity[item]

total_order_amount = sum(item_totals.values())

# ============solution=======================
print(f"Task 8:\n"
      f"Total big pizzas price: {item_totals["pizza_big"]} {currency}\n"
      f"Total medium pizzas price: {item_totals["pizza_medium"]} {currency}\n"
      f"Total juice price: {item_totals["juice"]} {currency}\n"
      f"Total cake price: {item_totals["cake"]} {currency}\n"
      f"Total water price: {item_totals["water"]} {currency}\n"
      f"Total order amount: {total_order_amount} {currency}\n"
      )

# ===========================================================================================================

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
# I've changed 232 photos quantity to 233 - to have more practice with this task
# =================given===========================
photos_quantity = 233
photos_per_page = 8
pages_used = photos_quantity / photos_per_page
pages_required = photos_quantity // photos_per_page + 1
#pages_required = int(pages_used) + 1

# ============solution=======================
print(f"Task 9:\n"
      f"Photos quantity: {photos_quantity}\n"
      f"Photos per one page: {photos_per_page}\n"
      f"Pages will be used: {photos_quantity} / {photos_per_page} = {pages_used}\n"
      f"Pages quantity required: {pages_required}\n"
      )

# ===========================================================================================================

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
# Once again task is modified with another trip distance to have more practice to do
# =================given===========================
trip_distance = 1599
consumption_distance = 100
consumption_volume = 9
tank_volume = 48

distance_unit = "km"
tank_unit = "l"

#     ====total consumption====
consumption_event = trip_distance / consumption_distance
total_consumption = int(consumption_event * consumption_volume)
tanks_required_float = total_consumption / tank_volume
tanks_required_int = int(total_consumption) // tank_volume + 1 # +1
# #consumption reserve will be less than 1km after 1599 kms passed with 3 tanks filled
# what can be not enough to get the gas station after reaching the destination


# ============solution=======================
print(f"Task 10:\n"
      f"Trip distance is: {trip_distance} {distance_unit}\n"
      f"Fuel consumptions is: {consumption_volume} {tank_unit} per {consumption_distance} {distance_unit}\n"
      f"Total fuel required:{trip_distance} / {consumption_distance} * {consumption_volume} = {total_consumption} {tank_unit}\n"
      f"Total tanks required: {total_consumption} / {tank_volume} ≈ {tanks_required_float} = {tanks_required_int}"
      )

# ===========================================================================================================