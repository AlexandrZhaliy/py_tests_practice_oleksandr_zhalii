from lesson_17.generators import even_numbers_generator, fibonacci_generator
from lesson_17.iterators import ReverseIterator, EvenFilterIterator
from lesson_17.decorators import logger, handle_exceptions

@logger
@handle_exceptions
def get_reverse_numbers(n):
    numbers = even_numbers_generator(n)
    reverse = ReverseIterator(numbers)
    return list(reverse)

@logger
@handle_exceptions
def get_even_fibonacci_numbers(n):
    numbers = fibonacci_generator(n)
    even_numbers = EvenFilterIterator(numbers)
    return list(even_numbers)

if __name__ == "__main__":
    reverse_numbers = get_reverse_numbers(10)
    fibonacci_even = get_even_fibonacci_numbers(50)
    print("\nFinal results:")
    print(f"Reverse even numbers: {reverse_numbers}")
    print(f"Even Fibonacci numbers: {fibonacci_even}")

