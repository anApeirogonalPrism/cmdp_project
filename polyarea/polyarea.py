import math
import time
import random


# highlight: \033[1m\033[3m\033[4m   \033[0m
class polyarea:
    class Poly:
        def __init__(self) -> None:
            self.polya = polyarea()
            self.Area = self.polya.Area()
            self.sys = self.polya.system()
            self.gu = self.sys.getunit()

            self.result = 0
            self.calc = ""

        def _poly(self):
            print("\nContents (choose): ")
            print("\033[1m\033[3m\033[4mTRI\033[0migon (regular) ")
            print("\033[1m\033[3m\033[4mQUAD\033[0mrilateral ")
            print("\033[1m\033[3m\033[4mPENTA\033[0mgon ")
            print("\033[1m\033[3m\033[4mHEXA\033[0mgon ")
            print("\033[1m\033[3m\033[4mHEPTA\033[0mgon ")
            print("\033[1m\033[3m\033[4mOCTA\033[0mgon ")
            print("\033[1m\033[3m\033[4mENNEA\033[0mgon ")
            print("\033[1m\033[3m\033[4mDECA\033[0magon ")
            print("\033[1m\033[3m\033[4mHENDEC\033[0magon ")
            print("\033[1m\033[3m\033[4mDODEC\033[0magon ")

            userInput = input()
            userInput = userInput.lower().strip()
            if userInput == "tri":
                try:
                    side = float(input("\nEnter a side length as a number: "))
                except ValueError:
                    print(
                        "An exception has occurred. It seems like you've entered a text instead of a number. Please retry "
                        "responsibly. "
                    )
                getUnit()
                result = Area(side, unit)
                result.triangle()
            elif userInput == "quad":
                try:
                    side = float(input("\nEnter a side length as a number: "))
                except ValueError:
                    print(
                        "An exception has occurred. It seems like you've entered a text instead of a number. Please retry "
                        "responsibly. "
                    )
                getUnit()
                result = Area(side, unit)
                result.quadrilateral()
            elif userInput == "penta":
                try:
                    side = float(input("\nEnter a side length as a number: "))
                except ValueError:
                    print(
                        "An exception has occurred. It seems like you've entered a text instead of a number. Please retry "
                        "responsibly. "
                    )
                getUnit()
                result = Area(side, unit)
                result.pentagon()
            elif userInput == "hexa":
                try:
                    side = float(input("\nEnter a side length as a number: "))
                except ValueError:
                    print(
                        "An exception has occurred. It seems like you've entered a text instead of a number. Please retry "
                        "responsibly. "
                    )
                getUnit()
                result = Area(side, unit)
                result.hexagon()
            elif userInput == "hepta":
                try:
                    side = float(input("\nEnter a side length as a number: "))
                except ValueError:
                    print(
                        "An exception has occurred. It seems like you've entered a text instead of a number. Please retry "
                        "responsibly. "
                    )
                getUnit()
                result = Area(side, unit)
                result.heptagon()
            elif userInput == "octa":
                try:
                    side = float(input("\nEnter a side length as a number: "))
                except ValueError:
                    print(
                        "An exception has occurred. It seems like you've entered a text instead of a number. Please retry "
                        "responsibly. "
                    )
                getUnit()
                result = Area(side, unit)
                result.octagon()
            elif userInput == "ennea":
                try:
                    side = float(input("\nEnter a side length as a number: "))
                except ValueError:
                    print(
                        "An exception has occurred. It seems like you've entered a text instead of a number. Please retry "
                        "responsibly. "
                    )
                getUnit()
                result = Area(side, unit)
                result.enneagon()
            elif userInput == "deca":
                try:
                    side = float(input("\nEnter a side length as a number: "))
                except ValueError:
                    print(
                        "An exception has occurred. It seems like you've entered a text instead of a number. Please retry "
                        "responsibly. "
                    )
                getUnit()
                result = Area(side, unit)
                result.decagon()

    # noinspection SpellCheckingInspection
    class Area:
        def __init__(self, a, unit):
            self.a = a
            self.unit = unit
            self.system = polyarea().system()

        def triangle(self):
            result = (math.sqrt(3) / 4) * self.a**2
            calculation = f"(√3 / 4) {self.a}²"
            init_ans(calculation, result, self.unit)

        def quadrilateral(self):
            result = self.a**2
            calculation = f"{self.a}²"
            init_ans(calculation, result, self.unit)

        def pentagon(self):
            result = (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.a**2
            calculation = f"1/4 * √(5 * (5 + 2 * √(5))) * {self.a}²"
            init_ans(calculation, result, self.unit)

        def hexagon(self):
            result = (3 * math.sqrt(3) / 2) * self.a**2
            calculation = f"3 * √(3) / 2 * {self.a}²"
            init_ans(calculation, result, self.unit)

        def heptagon(self):
            result = (7 / 4) * (self.a**2) * 2.07652139
            calculation = f"7/4 * {self.a}² * cot(180°/7)"
            init_ans(calculation, result, unit)

        def octagon(self):
            result = 2 * (1 + math.sqrt(2)) * self.a**2
            calculation = f"2 * (1 + √(2)) * {self.a}²"
            init_ans(calculation, result, unit)

        def enneagon(self):
            result = (9 / 4) * (self.a**2) * 2.74747741
            calculation = f"9/4 * {self.a}² * cot(180°/9)"
            init_ans(calculation, result, unit)

        def decagon(self):
            result = (5 / 2) * (self.a**2) * math.sqrt(5 + 2 * math.sqrt(5))
            calculation = f"5/2 * {self.a}² * √(5 + 2 * √(5))"
            init_ans(calculation, result, unit)

    class system:
        class init:
            def __init__(self, calculation, result, *, xtext) -> None:
                self.calc = calculation
                self.result = result
                self.xtext = xtext

            def ans(self):
                """Initiate answers

                Args:
                    calculation (str): e.g. 1 + 1
                    result (float): evaluate calculation
                    xText (str): any extra text added to the calculation
                """
                time.sleep(((random.randint(100, 200)) / 100))
                print("[|  ] Evaluating calculation...")
                time.sleep(((random.randint(50, 100)) / 100))
                print("[|| ] Preparing result...")
                time.sleep(((random.randint(100, 200)) / 100))
                print("[|||] Result completion successfully created!")
                time.sleep(((random.randint(65, 165)) / 100))
                print(f"{self.calc} = {self.result}{self.xtext}")

        class getunit:
            class request:
                def __init__(self) -> None:
                    self.unit = ""
                    self.units = ["mm", "cm", "m", "km"]

                def getUnit(self):
                    afu = str(input(""))

            class defaultunit:
                def __init__(self) -> None:
                    self.getUnit()
                    self.unit = "cm"

                def getUnit(self):
                    return self.unit
