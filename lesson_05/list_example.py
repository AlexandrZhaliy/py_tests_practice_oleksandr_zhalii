# list [] - mutable, iterable

my_list_names = ["Alex", "Den"]
print(id(my_list_names))
print(my_list_names)

my_list_names.append("Ivan")
print(id(my_list_names))
print(my_list_names)

print(my_list_names[0])
print(my_list_names[1:])
print(my_list_names[-1])
print(my_list_names[::-1])

#append
my_list_names.append("Viktor")
print(my_list_names)

#extend
additional_list =  [1, 2, 3]
my_list_names.extend(additional_list)
print(my_list_names)

#insert
my_list_names.insert(1, "Sofa")
print(my_list_names)

#pop
last_element = my_list_names.pop()
print(last_element)
print(my_list_names)

second_from_end = my_list_names.pop(-2)
print(second_from_end)
print(my_list_names)

#remove
my_list_names.append("Ivan")
print(my_list_names)
my_list_names.remove("Ivan")
print(my_list_names)

my_list_names = ["Alex", "Vasya", "Kolya", "Petya", "Viktor", "Vasya", "Petya"]
element_to_delete = "Vasya"
vasya_count = my_list_names.count(element_to_delete)

# variant 1
# list_of_vasya = []
# for element in my_list_names:
#     if element==element_to_delete:
#         list_of_vasya.append(element)
#
# for element in list_of_vasya:
#     my_list_names.remove(element)
#
# print(my_list_names)

# variant 2
while vasya_count > 0:
    my_list_names.remove(element_to_delete)
    vasya_count-=1

print(my_list_names)