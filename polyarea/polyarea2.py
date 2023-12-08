import math


class Cotangent(object):
    def __new__(self, x):
        return self.cot(self, x=math.degrees(x))

    def cot(self, x):
        tangent_value = math.tan(x)
        cotangent_value = 1 / tangent_value
        return cotangent_value


class polyarea(object):
    def reg_triangle(self, a):
        result = (math.sqrt(3) / 4) * (a**2)
        return [f"A = {result}", str(result)]

    def square(self, a):
        result = a**2
        return [f"A = {result}", str(result)]

    def pentagon(self, a):
        result = (1 / 4) * (math.sqrt(5 * (5 + 2 * (math.sqrt(5))))) * a**2
        return [f"A = {result}", str(result)]

    def hexagon(self, a):
        result = (3 * math.sqrt(3) / 2) * a**2
        return [f"A = {result}", str(result)]

    def heptagon(self, a):
        result = (7 / 4) * (a**2) * 2.07652139657
        return [f"A = {result}", str(result)]

    def octagon(self, a):
        result = 2 * (1 + math.sqrt(2)) * a**2
        return [f"A = {result}", str(result)]

    def enneagon(self, a):
        result = (9 / 4) * (a**2) * 2.74747741945
        return [f"A = {result}", str(result)]

    def decagon(self, a):
        result = (5 / 2) * (a**2) * (math.sqrt(5 + 2 * math.sqrt(5)))
        return [f"A = {result}", str(result)]


print(polyarea().heptagon(1)[1])
