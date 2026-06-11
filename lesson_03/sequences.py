string_sequence = "Hello Alex"
list_sequence = [0,2,3,5,7]
tuple_sequence = (1,2,3)
dict_sequence = {"name": "Alex", "age": 27}
set_sequence = {1, 2, 3, 4, "Hi"}
#len - this function returns sequence entities quantity

print(len(string_sequence))
print(len(list_sequence))
print(len(tuple_sequence))
print(len(dict_sequence))

print(string_sequence[0])
print(string_sequence[1])
# print(string_sequence[99])                    # IndexError: string index out of range
print(string_sequence[len(string_sequence)-1])  #picks the last element of string_sequence
print(string_sequence[-1])                      # also picks the last element of string_sequence

print(list_sequence[1])
print(tuple_sequence[1])
# print(set_sequence[1])                     # TypeError: 'set' object is not subscriptable - as set doesn't guarantee the order of items
# print(dict_sequence[0])                    # KeyError: 0 - as dictionary doesn't guarantee the order of items as well

print(string_sequence[2:9:2])                #[start(including):end(excluding):step]
print(string_sequence[0:10])                 #[start(including):end(excluding):step - default]
print(string_sequence[::2])                  #[start(including) - default :end(excluding) - default :step - 2]
print(string_sequence[:10:])                 #[start(including) - default :end(excluding) - default :step - default]
print(list_sequence[1:len(list_sequence)])   #starts to return elements with 1 first skipping????????????
