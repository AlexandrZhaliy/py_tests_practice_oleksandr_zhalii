# =================== HOMEWORK 6.1 =======================
# =========== user input receiving ==============
input_string_1 = input()
# test_1
# print(user_input_string)

# =========== received value analysis ===========
unique_symbols = []
for symbol in input_string_1:
    if symbol not in unique_symbols:
        unique_symbols.append(symbol)
# test_2
# print(unique_symbols)

unique_symbols_quantity = len(unique_symbols)
# test_3
# print(unique_symbols_quantity)

more_than_ten = False
if unique_symbols_quantity > 10:
    more_than_ten = True
else:
    more_than_ten = False
print(more_than_ten)