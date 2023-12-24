class employee:
    work = "BSCS department"
    salary = 478
    # address = "Karachi"
owais = employee()
saif = employee()

# salary_of_owais = 350000
# salary_of_ali = 42340000
print(employee.work)
print(employee.work)

employee.work = "Electrical Engineering Department"

print(employee.work)
print(employee.work)
print(owais.salary)
print(saif.salary)
print(employee.salary)

#Below line will throw an error because this adress is not available in class instance 
print(saif.address)