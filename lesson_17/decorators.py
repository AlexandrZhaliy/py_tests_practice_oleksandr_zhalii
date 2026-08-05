def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Input: {args}")
        result = func(*args, **kwargs)
        print(f"Output: {result}")
        return result
    return wrapper

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Error occurred: {error}")
            return None

    return wrapper