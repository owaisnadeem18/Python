
def func(num):
    try:

        a = int(input("Enter 1st Number = "))
        b = int(input("Enter 2nd Number = "))
        print(a+b)
        return 1 


    except:
        print("Enter Valid Input !!! ")
        return 0
        

    finally:
        print("I'll always get executed !!! ")
        return 1
        

print("This Is done !!! ")

print(func(45))