class employee:
    school = "Oxford School"
    # print(school)
    # print("o")
    # print("w")
    # print("a")
    # print("i")
    # print("s")

owais = employee()
samad = employee()
print(owais.school)
print(samad.school)

employee.school = "Ideal School"

print(owais.school)
print(samad.school)

print("*************Constructor Concept******************")
def __init__(self):
    print("Employee is created")


owais = employee()
