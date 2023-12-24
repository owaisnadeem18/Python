while(True):
    print('''Tap "q" to quit ...''')
    a = input("Enter a Number : ")
    if a=='q':
        break

    try:
        print("trying")
        a = int(a)
        if(a>5):        
            print("Your Number is greator than 05")

    except Exception as e:
        print(f"Your Error is {e}")

print("Thanks for playing")