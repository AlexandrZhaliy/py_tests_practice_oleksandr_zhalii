sent = "Alex My name is Alex"

list_of_words = sent.split()
print(list_of_words)

join_string = " cat ".join(list_of_words)
print(join_string)

join_string = "+".join(sent)
print(join_string)

# numbers = 1, 2, 3
# join_string = " cat ".join(numbers)
# print(join_string)                     # join works with strings only

print(sent.count("m"))