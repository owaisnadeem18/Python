# Snake , Water , Gun Game 

import random 

def gameWin(computer , you):
    if computer == you:
        return None
    # For all possible cases when computer will select 's'
    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    # For all possible cases when computer will select 'w'
    elif computer == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

    # For all possible cases when computer will select 'g'
    elif computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("It's Computer's Turn : and computer will select randamoly")
computer = random.randint(1,3)
if computer == 1:
    computer = 's'
elif computer == 2:
    computer = 'w'
elif computer == 3:
    computer = 'g'

you = input("It's Your's Turn select among (s) , (w) or (g)")
a = gameWin(computer , you)
print(f"Computer randamoly Selected = {computer}")
print(f"You Selected = {you}")

if a == None:
    print("It's a Tie !")
elif a:
    print("You won")
else:
    print("You Loose")