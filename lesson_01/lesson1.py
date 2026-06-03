print("Hello, world!")

my_int = 10
another_int =  20
my_float = 10.5

my_string = "Hello"
my_list = [1, 2, 3, 5.9, True, [1, 0]]
my_tuple = (1, 2, None)  # tuple is a constant list and cannot be changed #

my_set = {1, 2, False}
my_dict = {"key": "value", "key2": {"sub_key": "sub_value"}}

my_bool = True
my_none = None  # "null" entity analogue#

my_variable = None
print(my_variable)
my_variable = my_int + my_float
print(my_variable)

# ctrl + / - line commenting command

"""
comment
also can be 
assigned for multiple lines
with triple "
"""

# snake_case - variables names
# CamelCase - classes names
# UPPER_SNAKE - constants names

MY_VARIABLE = 10
print(MY_VARIABLE)
MY_VARIABLE = "Hello!"
print(MY_VARIABLE)

_ = "trash variable"

BASE_PAGE_URL = "example.com"

sum_ = 5 + 10
diff = 15 - 10
mult = 5 * 12
div = 50 / 5

# lower-score adds after variable's name which name is one of python's default commands
# ctrl + alt + l - adds spaces formatting

print(sum_)
print(diff)
print(mult)
print(div)

# = assigning operator
# == comparison operator , returns boolean true/false

if sum_ == 15:
    print("sum is equal to 15")
    if div == 0:
        print("divination is equal to 0")

my_name = "Alex"
print("Hello", my_name, sep="+")
print("Hello", my_name, end='')
print("Hello", my_name)

print("Hello my name is", my_name, "My age is", sum_ + 20)


my_int = 10
another_int =  20
my_float = 10.5

print(id(my_int))
print(id(another_int))
another_int = my_int
print(id(another_int))

my_float = 15.3

print(type(my_float))

my_sum = int(my_int + my_float)
print(my_sum)

my_sum = float(my_int + my_float)
print(my_sum)

my_sum = int(my_float)
print(my_sum)

my_int = 10
my_anotherint = 20
my_sum = float(my_int + my_anotherint)
print(my_sum)

my_name, my_age = "Alex", 30
print(my_name, my_age)

copy_age, copy_name = my_name, my_age
print(copy_age, copy_name)
