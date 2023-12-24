num = int(input("Enter any Number = "))

if(num==0):
    print("The number is zero")
elif(num>0):
    if(num<10):
        print("The number is less than 10 and it is in single digit ")
    elif(num==10):
        print("The number is equal to 10 and it is in double digit ")
    else:
        print("The number is greator than 10")
else:
    print("The number is less than 0 and it is a Negative Number ")
