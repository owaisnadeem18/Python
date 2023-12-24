class employee:
    company = "Google"
    pay = 50000
    def salary(self):
        print(f"The salary of this employee working in {self.company} is {self.pay}")

# Here banda is an object 

banda = employee()

banda.salary() # It will convert into { Employee.salary(banda) }