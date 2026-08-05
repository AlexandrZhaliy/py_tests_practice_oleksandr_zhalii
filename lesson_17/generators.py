def even_numbers_generator(n):
    for number in range(0, n + 1):
        if number % 2 == 0:
            yield number

# test
# numbers = even_numbers_generator(10)
#
# for num in numbers:
#     print(num)


def fibonacci_generator(n):
    a = 0
    b = 1

    while a <= n:
        yield a
        a, b = b, a + b

# test
# print(list(fibonacci_generator(20)))