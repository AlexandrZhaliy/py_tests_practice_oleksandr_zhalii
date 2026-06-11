#tuple () - immutable, iterable type

my_names = ("Alex", "Vasya", "Petya")
print(my_names)
print(my_names[0])
print(type(my_names))
print(id(my_names))

my_names = my_names + ("Vasya", "Kolya", "Petya")
print(my_names)
print(id(my_names)) # so if you want to add something to tuple, you'll receive another re-created tuple with another memory-id

for name in my_names:
    print(name)

print(my_names[1:])