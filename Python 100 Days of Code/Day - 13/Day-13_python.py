# Day : 13
# 100 Days of Code
# Topic : String Methods in python

# X---------------------------------------------------------------------------------X

a = "Owais !!!!! Ali Aslam"

print(a)
print(len(a))
print(a.replace("Owais", "Haris"))
print(a.upper())
print(a.lower())
print(a.strip("Owais"))
print(a.split())

heading = "introduction to Netflix Video SerIES"
print(heading.capitalize())

str = "Owais_is_a_Good_boy"

print(len(str))
print(str.center(500))
print(len(str.center(500)))
print(len(str.center(25)))

print(str.count("o"))
print(str.endswith("y"))

str2 = "Harry is a good boy"

print(str2.find("is"))
print(str2.find("Owais"))
# print(str2.index("Owais"))
str3 = "WelcomeToOnlineLearningWithOwais"
print(str3.isalpha())
str4 = "Welcometoonlinelearningwithowais345"
print(str4.isalnum())
eid = "We Wish you Eid Mubarak\n"
print(eid.isprintable())
eid = "We Wish you Eid Mubarak"
print(eid.isprintable())
str5 = "        "
print(str5.isspace())
str5 = ""
print(str5.isspace())
str5 = "My name is Owais"
print(str5.isspace())
str6 = "World Wide Web"
print(str6.istitle())
str6 = "World Wide Web is something"
print(str6.istitle())

print(str6.swapcase())

print(str6.startswith("World"))
print(str6.startswith("world"))

str07 = "owais is learning python"
print(str07.title())
