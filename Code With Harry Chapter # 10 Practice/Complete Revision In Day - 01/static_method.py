class employee:
    company = "Google"
    pay = 50000
    def salary(self , signature):
        print(f"The salary of this employee working in {self.company} is {self.pay} \n{signature}")

# # Here banda is an object 

banda = employee()

banda.salary("hy") # It will convert into { Employee.salary(banda) }

class employee:
    company = "Google"
    pay = 50000

    @staticmethod
    def greet():
        print("Good Morning")

# Here banda is an object 

banda = employee()
banda.greet()