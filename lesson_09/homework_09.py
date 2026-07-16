# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.


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