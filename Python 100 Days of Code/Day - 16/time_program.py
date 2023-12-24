import time 

a = input("Enter Your Name = ")

time = time.strftime('%H:%M:%S')

print(time)

b = time.strftime('%H')

if b < "12":
    print("Good Morning")
elif "12" < b < "17":
    print("Good Afternoon")
else:
    print("Good Evening")
