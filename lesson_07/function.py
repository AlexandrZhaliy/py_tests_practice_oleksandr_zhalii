def greeting(first_name: str, second_name: str):
    print(f"Hello {first_name} {second_name}")

# def div_two_elements(first, second):
#     return first / second

# for  full_name in [("Oleksandr, Zhalii"), ("John", "Smith")]:
    # greeting(full_name[0], full_name[1])
#
# for full_name in [("Oleksandr, Zhalii"), ("John", "Smith")]:
#     greeting(first_name=full_name[0], second_name=full_name[1])
#
# print(div_two_elements(10, 5))

def get_greeting(first_name: str, second_name: str) -> str:
    """

    :param first_name:
    :param second_name:
    :return: full_greeting
    """
def sum_all_elements(number1,number2, number3):
    return sum([number1, number2, number3])
print(sum_all_elements(1, 2, 3))

# * - args
def sum_all_elements(*numbers):
    print("Numbers: ", numbers)
    return sum(numbers)
print(sum_all_elements(1,2,3,2,5,*[41,2,5]))

def sum_all_elements(double_arg, *args):
    print("double arg: ", double_arg)
    print("Numbers: ", args)
    return sum(args) + double_arg*2
print(sum_all_elements(1,2,3,2,5,*[41,2,5]))

def sum_all_elements(double_arg, *args, ignore_args):
    print("double arg: ", double_arg)
    print("Numbers: ", args)
    print("Ignore number: ", ignore_args)
    numbers = [k for k in args if k != ignore_args]

    return sum(numbers) + double_arg + 2
# print(sum_all_elements(1,2,3,2,5,*[41,2,5]))

# ** - kwargs
def sum_all_elements(double_arg, *args, ignore_args=5, **kwargs):
    print("double arg: ", double_arg)
    print("Numbers: ", args)
    print("Ignore number: ", ignore_args)
    print("kwargs: ", kwargs)
    numbers = [k for k in args if k != ignore_args]

print(sum_all_elements(1, 2, 3,2,5,*[41, 2, 5], ignore_args=41, double_all=True))


def sum_all_elements(double_arg, *args, ignore_args=5, **kwargs):
    print("double arg: ", double_arg)
    print("Numbers: ", args)
    print("Ignore number: ", ignore_args)
    print("kwargs: ", kwargs)
    numbers = [k for k in args if k != ignore_args]
    result = sum(numbers) + double_arg * 2
    if kwargs.get("double_all"):
        result = result *  2
    return result

my_arguments = {"arg1": "value", "double_all": True, "additional_list": [1,2,3]}

print(sum_all_elements(1, 2, 3,2,5,*[41, 2, 5], ignore_args=41, double_all=True))