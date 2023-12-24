# Class Method 

class Employee:
    company = "Google"
    location = "USA"
    salary = "100000"

    @classmethod
    def changeSalary(cls , sal):
        cls.salary = sal


e = Employee()

print(e.salary)

e.changeSalary(50000)
print(e.salary)