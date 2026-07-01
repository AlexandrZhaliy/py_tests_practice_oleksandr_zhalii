# # a = [1, 2, 3, 4, 5, 6, 7, 8]
# # # x = len(a)
# # # x = 5 in a
# # # x = a.sort()
# # x = a[::2]
# # print(x)
#
#
# # t = (1, 2, 3, 4, 5, 6, 7, 8)
# # a, b, c, = (1, 2, 3)
# # print(a, b, c)
#
# # user = {"name": "Alex", "age": 30}
# # x = user["name"]
# # print(x)
# # x = user.get("name")
# # print(x)
# # user = {"name": "Alex", "age": 30}
# # user["name"] = "Petya"
# # user["city"] = "Kyiv"
# # user.pop("name")
# # print(user)
# #
# # @decorator
# # x = 15 and 2
# # print(x)
#
# # for x in[1, 2, 3]:
# #     print(x)
# #
# # users = ["Alex", "Bob", "John"]
# #
# # for user in users:
# #     print(user)
# #
# # word = "Python"
# # index = 0
# # while index < len(word):
# #     print(word[index])
# #     index += 1
# #     print(index)
#
# # users = ["Vasya", "Kolya", "Petya"]
# # for char in users:
# #     print(char)
# #
# # user_data = {"name": "Vasya"}
# # for hui in user_data.items():
# #     print(hui)
#
#
# # user_data = ["Vasya", "Kolya", "Petya"]
# # for zhopa_losya in user_data:
# #     print(zhopa_losya)
# #
# # numbers = [1, 2, 3, 4, 5]
# # for zhopa_bobra in numbers:
# #     print(zhopa_bobra)
#
# json_data = {
#   "users": {
#     "vasya_id": [
#       {
#         "name": "Vasya",
#         "age": 18,
#         "city": "Kyiv"
#       }
#     ],
#     "petya_id": [
#       {
#         "name": "Petya",
#         "age": 20,
#         "city": "Kharkiv"
#       }
#     ]
#   },
#   "cars": {
#     "civil_cars": {
#       "volvo_id": [
#           {
#             "maker": "Volvo",
#             "model": "T-146",
#             "type": "sedan"
#           }
#         ],
#       "toyota_id": [
#           {
#             "maker": "Toyota",
#             "model": "Supra",
#             "type": "pushka_gonka_raketa"
#           }
#         ]
#       },
#     "warfare_cars": {
#       "tank": [
#         {
#           "name": "Abrams",
#           "model": "A-1"
#         }
#       ],
#       "btr": [
#           {
#             "name": "Bradley",
#             "model": "M-113"
#           }
#         ]
#       }
#     }
# }
#
# x = json_data.keys()
# print(x)
#
# def function_name (a, b):
#     return f"{int(a)} {str(b)}"
#
#
# output = function_name(17, "years")
# print(output)
#
#
# def user_data(**profile):
#     return f"User info ", profile["age"]
#
# x = user_data(name = "Vasya", age = 18)
#
# print(x)
#
# y = 3
# square = lambda y: 3*3
# y = 3
# print(square(3))
#

class Shpatel:                                      # this is a class
    def __init__(self, material, width):            # this is attributes setting method
        self.material = material
        self.width = width

    def make_a_cake(self):                          # this is simple, action doing method
        return "Making a cake edge"

    def repair_a_wall(self):                        # and another one simple, action doing method
        return "Repairing a wall"

shpatel_culinary = Shpatel("plastic", 80) # this is an object, created in context with a class.
                                                        # He also sets his data via attributes receiving __init__ method

cook = shpatel_culinary.make_a_cake()                   # here we use our object to perform an action using action method

shpatel_build = Shpatel("metal", 120)

wall_repairing = shpatel_build.repair_a_wall()

print(cook)
print(wall_repairing)
