# Write a Program in which print multiplication table
#  of a number using multiplication table with for loop

# Question : 01 

number = int(input("Enter a number = "))
for i in range(1 , 11):
    # print(str(number) + "X" + str(i) + "=" + str(number*i)) 
        # OR 
    print(f"{number} * {i} = {number * i}")


