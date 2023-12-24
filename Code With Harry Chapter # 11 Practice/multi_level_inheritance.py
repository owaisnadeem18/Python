# Multi Level Inheritance 
# In this inheritance we see step by step inherited classes 

class programmer1:
    country = "Pakistan"
    name = "Owais"
    print("I'm Programmer # 01")
    def show(self):
        print(f"The Salary of this man is = 45000 ")

    def check_data(self):
        print(f"The Salary of this man is = 10,000 ")

class programmer2(programmer1):
    height = "160 cm"

    def salary(self):
        print("The salary of this programmer is 90k")

class programmer(programmer2):
    company = "google"

    def show(self):
        print(f"The Salary of this man is = 45000 ")

obj1 = programmer1()

obj1.check_data()

obj2 = programmer2()

obj2.salary()
obj2.check_data()

obj3 = programmer()

obj3.check_data()
obj2.show()


obj2.show()