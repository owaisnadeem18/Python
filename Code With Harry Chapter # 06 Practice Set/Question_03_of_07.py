
# Write a Program in which check whether the program is spam or not .

text = input("Enter Your Text : ")

if("make money online" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click to earn" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam\n")
else:
    print("This text is not spam\n") 