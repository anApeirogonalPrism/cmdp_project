import math
from fractions import fractions




class fms:
    def __init__(self) -> None:
        pass

    class Pythagorean_Theorem:
        def __new__(self, a: float, b: float) -> float:
            return self.__pt__(self, a, b)

        def __pt__(self, a: float, b: float) -> float:
            return str((math.sqrt(a**2 + b**2)))

    class sqrt(object):
        def __new__(self, x: float) -> float:
            return self.__sqrt(self, x)

        def __sqrt(self, x: float) -> float:
            try:
                return math.sqrt(x)
            except Exception as e:
                raise MathError(e)

    class quadratic:
        def __new__(self, a: float, b: float, c: float) -> list[float, float]:
            return self.__q(self, a, b, c)

        def __q(self, a: float, b: float, c: float) -> list[float, float] | list[float]:
            if a == 0:
                raise MathError("a cannot be 0")
            if b**2 - (4 * a * c) >= 0:
                A = (-b + math.sqrt(b**2 - (4 * a * c))) / (2 * a)
                if type(A) == float:
                    A = str(Fraction(A).limit_denominator())
                B = (-b - math.sqrt(b**2 - (4 * a * c))) / (2 * a)
                if type(B) == float:
                    B = str(Fraction(B).limit_denominator())
                return [A, B]
            elif b**2 - (4 * a * c) == 0:
                x = (-b) / (2 * a)
                if type(x) == float:
                    x = str(Fraction(x).limit_denominator())
                return x
            else:
                raise MathError("there are no solutions.")

    class trigonometric_funcs:
        """This uses radians as parameters, so make sure that you convert your arguments to radians
        for this class."""

        class sine:
            def __new__(self, x):
                return self.__sine(self, x)

            def __sine(self, x):
                return math.sin(x)

        class cosine:
            def __new__(self, x):
                return self.__cosine(self, x)

            def __cosine(self, x):
                return math.cos(x)

        class tangent:
            def __new__(self, x):
                return self.__tangent(self, x)

            def __tangent(self, x):
                return math.tan(x)

        class cotangent:
            def __new__(self, x):
                return self.__cotangent(self, x)

            def __cotangent(self, x):
                return (math.cos(x)) / (math.sin(x))

        class secant:
            def __new__(self, x):
                return self.__secant(self, x)

            def __secant(self, x):
                return 1 / math.cos(x)

        class cosecant:
            def __new__(self, x):
                return self.__cosecant(self, x)

            def __cosecant(self, x):
                return 1 / math.sin(x)
