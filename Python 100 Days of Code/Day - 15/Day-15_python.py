# Day : 15
# 100 Days of Code 
# Topic : Exercise # 02 in python 
# Use time zone in python to greet your User according to time  

# X---------------------------------------------------------------------------------X

import time
name = input("Enter Your Name:- ")
currentTime = time.strftime('%H:%M:%S')
print(currentTime)
hour = time.strftime('%H')

if hour < "12":
    print("Good Morning", name)
elif "12" < hour < "17":
    print("Good Afternoon", name)
else:
    print("Good Evening", name)