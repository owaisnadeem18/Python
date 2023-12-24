# By using recursion print sum of 10 natural numbers

def sum(n):
    if n <= 1:
        return n
    else:
        return n + int(sum(n-1))

n = int(input("Enter a number = "))

# a = sum(5)

print("The sum of n even numbers is " , sum(n))