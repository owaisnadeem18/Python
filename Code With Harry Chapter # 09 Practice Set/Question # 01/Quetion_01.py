a = open('poems.txt')

b = a.read()

if 'twinkle' in b:
    print("Present")
else:
    print("Not Present")
print(b)
a.close()