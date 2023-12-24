class student:
    school = "Oxford School"
    address = "Green Town"
    # result = 80 

owais = student()
samad = student()



print(owais.school)
print(samad.school)
student.school = "Ideal School"

print(owais.school)
print(samad.school)

# print(owais.result) 
# print(samad.result) 

owais.result = 65
samad.result = 90

print(owais.result)
print(samad.result)

# print(owais.result) 
# print(samad.result) 

# It will throw an error if we do not have object attribute and 
# and even class attribute here in the below line 

print(samad.address)

# First our .py compiler finds out our object attribute 
# to print the value , but in case if it is not availabe
# then it always go towards the class attribute and in case 
# even if it is also no present , then we must have to face 
# an error here . 

# Instance Attribute = Object Attribute 
# Instance Class = Class Attribute 

# X------------------------------------------------------X