
letter = '''Dear "NAME"
I would like to congratulate you that you have gotten recommendation from PMA Long Course 150 L/C ISSB
and Today you are selected for Pakistan Military Academy 
Congratulations and Best of Luck . Regards Pakistan Army 
DATE ''' 

name = input("Enter Your name : ")
date = input("Enter Date : ")

letter = letter.replace("NAME" , name)
letter = letter.replace("DATE" , date) 

print(letter)