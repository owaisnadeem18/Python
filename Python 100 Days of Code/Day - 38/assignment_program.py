a = input ("Enter any number value between 5 and 9 or enter quit \n>>")
try: 
   if (int(a)<5 and int(a)>9):
           raise ValueError("The number is either lesser than 5 or bigger than 9")
except:
        if a!= "quit":
                 raise ValueError ("You entered a string other than quit")

                 