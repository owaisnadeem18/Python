# Question # 02 
# Here , in this question we've to find out the square , cube and square root of a number using OOP 

class Calculator():
    def __init__(self , num):
        self.number = num

    def square(self):
        print(f"The Square of {self.number} is {self.number **2}")

    def square_root(self):
        print(f"The Square Root of {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"The Cube of {self.number} is {self.number **3}")

check = Calculator(9)

check.square()
check.square_root()
check.cube()