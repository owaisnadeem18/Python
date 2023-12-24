# Day - 36 
# Exception Handling

try:
    table = input("Enter a number = ")
    print(f"The Multiplication Table of {table} : ")

    for i in range(1,11):
        print(f"{table} X {i} = {(int)(table) * i}")

# except:
#     print("Invalid Input!!!")

except ValueError as e:
    print(f"{e} Please Enter Valid Input!!! ")

print(f"We've successfully printed the multiplication table of {table}")