# Exercise # 02 Solution and understanding

import time

t = time.strftime('%H : %M : %S')

print(t)
hour = int(time.strftime('%H'))

hour = int(input("Enter Hours : "))

# print(hour)

if(hour>=6 and hour<12):
    print("Good Morning!!!")

elif(hour>=12 and hour<15):
    print("Good AfterNoon !!!")

elif(hour>=15 and hour<18):
    print("Good Evening!!!")

elif(hour>=18 and hour<23):
    print("Good Night!!!")

elif(hour>=0 and hour<4):
    print("Good Night!!!")