# Write a Program in which print the factorial of a number using for loop
# Factorial = 1 * 2 * 3 * 4 * 5 * ..... * n! 

from math import factorial


a = int(input("Enter a number "))

factorial = 1 

for b in range(1,a+1):
    factorial = factorial*b

print(f"The Factorial of {a} is = {factorial}")