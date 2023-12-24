# Write a Program in which check either the entered number is prime or not
# Question 04 

num = int(input("Enter a Number = "))

prime = True
for prime in range(2 , num):
    if(num % prime == 0):
        prime = False 
        break

if prime:
    print("The number is prime")  
else: 
    print("The number is non prime")   