# =================== HOMEWORK 6.4 =======================
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 155, 3571, 94586]
even_numbers = []

for  number in numbers:
    if number %2 == 0:
        even_numbers.append(number)
# test_1
# print(even_numbers)

print(sum(even_numbers))

