# Write a Program in which check whether a given number is prime or not 

a = int (input("Enter a number = "))

prime = True

for b in range(2, a):
    if (a%b == 0):
        prime = False
        break

if prime:
        print("Number is a prime ") 
else:
        print("Number is not a prime ")