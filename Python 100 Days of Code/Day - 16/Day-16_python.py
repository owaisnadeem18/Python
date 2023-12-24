# Day : 16
# 100 Days of Code 
# Topic : Match Case Statement in Python 

# X---------------------------------------------------------------------------------X

a = int(input("Enter value for a between 01 and 05 = "))

match a:
    case 1:
        print(f"The value of a is {a}")
    case 2:
        print(f"The value of a is {a}")
    case 3:
        print(f"The value of a is {a}")
    case 4:
        print(f"The value of a is {a}")
    case 5:
        print(f"The value of a is {a}")
    # case _ if a!= 90 :
    #     print(a , f"Out of Range number which is {a} and also not 90")
    case _ if a != 80 :
        print(a , f"Out of Range number which is {a} ")
    case _ if a != 70 :
        print(a , f"Out of Range number which is {a} and also 70")
