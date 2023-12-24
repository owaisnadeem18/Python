
# Write a program in which accept 6 students marks and then organize these marks in sorted form 

stud1 = int(input("Enter 1st student marks = "))
stud2 = int(input("Enter 2nd student marks = "))
stud3 = int(input("Enter 3rd student marks = "))
stud4 = int(input("Enter 4th student marks = "))
stud5 = int(input("Enter 5th student marks = "))
stud6 = int(input("Enter 6th student marks = "))

marks_list = [stud1 , stud2 , stud3 , stud4 , stud5 , stud6] 

# print(marks_list)

marks_list.sort()   

print(marks_list)
