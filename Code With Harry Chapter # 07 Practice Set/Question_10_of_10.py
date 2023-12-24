

print("XXXXX------Multiplication Table of a Number------XXXXX")
a = int(input("Enter a Number = ")) 


for b in range(25 , 0 , -1):

    # print(str(a*b) + " X " + str(a) + " = " + str(b))
    print(f"{a} * {b} = {a*b}")