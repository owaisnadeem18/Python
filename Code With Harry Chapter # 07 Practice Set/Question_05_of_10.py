# Write a program to find sum of 10 natural numbers using while 

a = int(input("Enter a number : ")) 
sum = 0
b = 1
while(b<=a): 
          sum = sum+b
          b = b + 1
    
print("This is the addition of" , a , "Even Numbers = " , sum)