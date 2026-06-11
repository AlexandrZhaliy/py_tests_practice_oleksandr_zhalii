name = "Alex"
print(id(name))

name= name + "Zhalii"
print(id(name))

#mutable types - list,  dict, set, bytearray
my_list_names = ["Alex", "Vasya"]
print(id(my_list_names))
print(my_list_names)

my_list_names.append("Ivan")
print(id(my_list_names))
print(my_list_names)