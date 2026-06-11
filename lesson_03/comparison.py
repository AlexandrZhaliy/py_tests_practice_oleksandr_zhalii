name = 'Alex'
age = 27

# 1 - True
# 0 - False

# & - and
# | - or
# "and" and "or" symbols require arguments to be placed inside the () brackets

# for &
# 1 1 - True
# 0 1 - False
# 1 0 - False
# 0 0 - False

# for |
# 1 1 - True
# 0 1 - True
# 1 0 - True
# 0 0 - False

if name=="Alex" and age == 27:
    print("Hello, Alex")

if (name=="Alex") & (age == 27):
    print("Hello, Alex")

if name=="Alex" or age == 28:
    print("Hello, Alex")

if (name=="Alex") | (age == 28):
    print("Hello, Alex")

# != - is NOT

if (name != "Vasya") & (age != 99):
    print("Hello, Alex")