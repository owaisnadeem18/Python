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
