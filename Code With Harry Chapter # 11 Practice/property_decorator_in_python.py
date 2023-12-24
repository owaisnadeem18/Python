class employee:
    company = "PIA"
    salary = 4400
    salary_bonus = 5600

    @property # This is also called as a getter method 

    def totalsalary(self):
        return self.salary + self.salary_bonus

    @totalsalary.setter
    def totalSalary(self , val):
        self.salary_bonus = val - self.salary

e = employee()
print(e.totalsalary)

e.totalSalary = 5600 

print(e.salary)
print(e.salary_bonus)


