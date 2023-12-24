
class student:
    field = "Google" #It is a class Attribute 

Owais = student() 
Saif = student()

salary_of_owais = 300000
salary_of_saif = 600000

a = student.field

print(a)
print(a)

student.field = "Youtube" 
print(student.field)
print(student.field)