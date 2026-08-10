# ====================== old version ==========================
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Input: {args}")
#         result = func(*args, **kwargs)
#         print(f"Output: {result}")
#         return result
#     return wrapper
#
# def handle_exceptions(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as error:
#             print(f"Error occurred: {error}")
#             return None
#
#     return wrapper
#

# =========== new version (imported logger used)=================
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Input: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Output: {result}")
        return result
    return wrapper

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            logger.exception(f"Error occurred: {error}")
            return None
    return wrapper