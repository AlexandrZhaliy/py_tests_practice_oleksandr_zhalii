class ReverseIterator:
    def __init__(self, iterable):
        self.collection = list(iterable)
        self.index = len(self.collection) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.collection[self.index]
        self.index -= 1
        return value

# test_01
# from generators import even_numbers_generator
# numbers = even_numbers_generator(10)
# reverse = ReverseIterator(numbers)
#
# for number in reverse:
#     print(number)

# =================================================================================

class EvenFilterIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            value = next(self.iterator)
            if value % 2 == 0:
                return value

# test_02
# from generators import fibonacci_generator
# numbers = fibonacci_generator(50)
# even_numbers = EvenFilterIterator(numbers)
#
# for number in even_numbers:
#     print(number)
