my_list_names = ["Alex", "Vasya", "Kolya", "Petya", "Viktor"]
my_list_ages = [1, 5, 18, 7, 95]

sorted_names = sorted(my_list_names)
sorted_ages = sorted(my_list_ages)

print(sorted_names, sorted_ages)

sorted_names_reverse = sorted(my_list_names, reverse=True)
sorted_ages_reverse = sorted(my_list_ages, reverse=True)

print(sorted_names_reverse, sorted_ages_reverse)

print(my_list_names, my_list_ages)

my_list_names.sort()
my_list_ages.sort()

print(my_list_names)
print(my_list_ages)

def my_fn(word):
    word_length = len(word)
    return word_length

#lambda arg: action with arg
sorted_names_custom_lambda = sorted(my_list_names, key=lambda x: len(x))
sorted_names_custom = sorted(my_list_names, key=my_fn)

print(sorted_names_custom_lambda, sorted_names_custom)