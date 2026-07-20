# ================= function_01 (Ref: homework_11) =================
def sum_numbers(string):
    try:
        result = 0
        for number in string.split(","):
            result += int(number)
        return result

    except ValueError:
        return "Не можу це зробити!"

# strings = [
#     "1,2,3,4",
#     "1,2,3,4,50",
#     "qwerty1,2,3"
# ]
#
# for string in strings:
#     print(sum_numbers(string))

# ================= function_02 (Ref: homework_09) =================
class Rhombus:
    def __init__(self, side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a


    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side value should be more than zero")
            object.__setattr__(self, name, value)
            return

        elif name == "corner_a":
            if value <= 0 or value >=180:
                raise ValueError("Rhombus corner should be between 0-180 degrees")
            object.__setattr__(self, name, value)
            object.__setattr__(self, "corner_b", 180 - value)
            return

        elif name == "corner_b":
            raise AttributeError("corner_b manual adding is restricted")
        object.__setattr__(self, name, value)


# # tests
# rhombus1 = Rhombus(1000, -50)
#
# print(rhombus1.side_a)
# print(rhombus1.corner_a)
# print(rhombus1.corner_b)

# ================= function_03 (Ref: homework_03, task_10) =================
def fuel_required(trip_distance, consumption_distance, consumption_volume):
    """Calculates how much fuel required for defined distance trip according a car's consumption (litres per 100 km)"""
    """Result returned in full litres to cover 100% of path"""
    total_consumption = trip_distance / consumption_distance * consumption_volume
    return int(total_consumption +1)

def tanks_required(fuel_required, tank_volume):
    """Calculates how much tank-fillings required for defined distance, consumption l/km and tank volume"""
    """Result returned in full tanks to cover 100% of path"""
    """Warning! Calculation does not apply to the remaining fuel reserve."""
    return fuel_required/tank_volume

# print(fuel_required(1599, 100, 9))
# print(tanks_required(fuel_required(1599, 100, 9), 48))

# ================= function_04 (Ref: homework_03, task_8) =================
def order_price_calculator(items):
    """This function calculates total order amount for list of tuples with items, quantity and price"""
    total = 0
    for name, quantity, price in items:
        total += price * quantity
    return total

# items = [
#     ("Піца велика", 4, 274),
#     ("Піца середня", 2, 218),
#     ("Сік", 4, 35),
#     ("Торт", 1, 350),
#     ("Вода", 3, 21)
# ]

# print(order_price_calculator(items))