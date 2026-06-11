string_example = "Placeholder"
tuple_example = (1,2,3)
list_string = list(string_example)
tuple_to_list = list(tuple_example)
print(list_string)
print(tuple_to_list)

my_numbers = [1, 2, 3]
# [what / where / at what condition]
list_comprehended = [num ** 2 for num in my_numbers if num % 2 == 1]
print(list_comprehended)

sq_list = []
for num in my_numbers:
    if num % 2 == 1:
        sq_list.append(num**2)
print(list_comprehended)
print(sq_list)

my_range_num = range(10)
print(list(my_range_num))

my_range_num_2 = range(10, 20)
print(list(my_range_num_2))

my_range_num_3 = range(10, 20, 2)
print(list(my_range_num_3))

sq_list_100 = [k**2 for k in range(1, 100)]
print(sq_list_100)
