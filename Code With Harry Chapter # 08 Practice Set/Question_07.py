
# Strip = If you wanna remove the spaces of any string
# then you can easily use it and your compiler will ignore
# all spaces

def remove_and_sprit(string , word):
        new_str = string.replace(word , "")
        return new_str.strip()

a = "       Owais you're a good boy        "
n = remove_and_sprit(a , "Owais")
print(n)
# print(a)
# print(a.strip())