marks = int(input("Enter Your Marks : ")) 

if marks>=90 and marks<=100 :
    Grade = "A++"
elif marks>=80 and marks<=100 :
    Grade = "A+"
elif marks>=70 and marks<=100 :
    Grade = "A"
elif marks>=60 and marks<=100 :
    Grade = "B"
elif marks>=50 and marks<=100 :
    Grade = "C"
elif marks>=40 and marks<=100 :
    Grade = "D"
elif marks>100:
    print("You are Extra Ordinary")
else:
    print("you are fail") 

print("Your Grade is " + Grade)