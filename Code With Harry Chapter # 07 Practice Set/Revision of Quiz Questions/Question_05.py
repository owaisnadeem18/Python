# Question : 05 
# Write a Program in which calculate the sum of 'n' Natural numbers using while loop

a = int(input("Enter a number = "))

sum = 0 
b = 1 

while (b <= a):
    sum = b + sum 
    b = b + 1

print("The addition of " , a , "Even Numbers = " , sum)
