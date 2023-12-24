# Write a Program in Which entered four numbers by user and find the greatest numbers among them 

a = int(input("Enter a number 1 = "))
b = int(input("Enter a number 2 = "))
c = int(input("Enter a number 3 = "))
d = int(input("Enter a number 4 = "))

if(a>b and a>c and a>d):
    print("a is the greatest number") 
elif(b>a and b>c and b>d): 
    print("b is the greatest number") 
elif(c>a and c>b and c>d): 
    print("c is the greatest number") 
elif(d>a and d>b and d>c): 
    print("d is the greatest number") 

# X-----------------------------------------------------------------------------X

a = int(input("Enter a number 1 = "))
b = int(input("Enter a number 2 = "))
c = int(input("Enter a number 3 = "))
d = int(input("Enter a number 4 = "))

if a>d:
    winner_1 = a 
else:
    winner_1 = d

if b>c:
    winner_2 = b 
else:
    winner_2 = c

if winner_1>winner_2: 
    print(str(winner_1) + " is greatest")
else: 
    print((str(winner_2) + " is greatest")) 