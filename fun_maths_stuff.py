import math
from custom_errors import MathError


class fms:
    def __init__(self) -> None:
        pass

    class Pythagorean_Theorem:
        def __new__(self, a: float, b: float) -> float:
            return self.__pt__(self, a, b)

        def __pt__(self, a: float, b: float) -> float:
            return float(math.sqrt(a**2 + b**2))

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
        
        def __q(self, a: float, b: float, c:float) -> list[float, float]:
            if a == 0:
                raise KeyError
            A = (-b + math.sqrt(b**2 - (4*a*c)))/(2*a)
            B = 


f = fms()
print(f.sqrt(4))
