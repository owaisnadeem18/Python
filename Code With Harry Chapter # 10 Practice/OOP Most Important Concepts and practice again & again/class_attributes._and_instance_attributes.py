# Class Attributes 

class employee:
    a = "Google"

b = employee()
c = employee()

b.salary = 30000
c.salary = 40000
print(b.a)
print(b.a)

employee.a = "Youtube"
print(b.a)
print(b.a)

print(b.salary)
print(c.salary)