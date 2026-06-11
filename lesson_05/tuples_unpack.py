my_names, vasya_name, petya_name = ("Alex", "Vasya", "Petya")
print(vasya_name)

my_names = ("Alex", "Vasya", "Petya")
print(*my_names) # unpacked as a separate values

print(my_names) # returned as a tuple

# my_name, not_my_name = ("Alex", "Vasya", "Petya") #not all paired - it'll cause an error
my_name, *not_my_name, kolya_name = ("Alex", "Vasya", "Petya", "Kolya")
print(my_name)
print(not_my_name)
print(kolya_name)

placeholder_text = "placeholder"

tuple_text = tuple(placeholder_text)
print(tuple_text)
