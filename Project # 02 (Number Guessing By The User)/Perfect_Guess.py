import random

randNumber = random.randint(1,100)

print(randNumber)
user_guess = None
guesses = 0 
while(user_guess!=randNumber):   

    user_guess = int(input("Enter your Guess = "))
    guesses += 1

    if (user_guess == randNumber):
         print("You Guessed it right !")

    else:
        if(user_guess>randNumber):
            print("You Guessed It Wrong !!! Enter a smaller number")
        else:
            print("You Guessed It Wrong !!! Enter a larger number")

print(f"You Guessed the correct Number in {guesses} guesses")

with open("hiscore.txt" , "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You've just broken the highest score! ")
    with open('hiscore.txt' , 'w') as f:
        f.write(str(guesses))