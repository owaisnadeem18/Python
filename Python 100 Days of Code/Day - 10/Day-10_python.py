# Day : 10
# 100 Days of Code
# Topic : Taking Input from User

#  X--------------------------------------------------------------------------------X

a = input("Enter 1st Number : ")  # Took input from user
b = input("Enter 2nd Number : ")  # Took input from user

# But this taken input value will be considered as of string type

# prove :

print(type(a))
print(type(b))

print(a+b)

# Now convert this string into Integer by the help of typecasting function :

a = int(a)
b = int(b)

print(a+b)

print(type(a))
print(type(b))

# Taking User Input means to ask for a result from your user

# This input function will must be a string number
a = input("enter your fvrt number = ")

# Note : If you wanna add two integer numbers , then you must have to type cast it , into integer

print("Your fvrt number is = " + a)
