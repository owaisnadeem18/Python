# Question # 04
# Here , in this question we've to find out the square , cube and square root of a number using OOP . But , here you also have to welcome your user that is using this calculator 

class Calculator():
    def __init__(self , num):
        self.number = num

    def square(self):
        print(f"The Square of {self.number} is {self.number **2}")

    def square_root(self):
        print(f"The Square Root of {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"The Cube of {self.number} is {self.number **3}")

    @staticmethod
    def greet():
        print("************Hello there to the best Calculator for square , square root and Cube in Python************")

check = Calculator(16)

check.greet()
check.square()
check.square_root()
check.cube()