# Write a program in which tell whether a student is passed or not 

a = int(input("Enter your marks of computer science "))

b = int(input("Enter your marks of Physics "))

c = int(input("Enter your marks of Chemistry "))

total_percentage = ((a+b+c)*100)/300
print(total_percentage)
if (a<33 or b<33 or c<33):
    print("You are failed because of less marks in one subject")
elif(total_percentage < 40):
     print("You are failed because of less percentage")
if(total_percentage == 40 and a == 33): 
    print("You are passed")
elif(total_percentage == 40 and b == 33):
    print("You are passed")
elif(total_percentage == 40 and c == 33):
    print("You are passed")
else:
    print("You are not passed / You are failed and not promoted in next class")