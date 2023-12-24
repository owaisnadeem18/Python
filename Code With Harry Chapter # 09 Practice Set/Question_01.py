a = open('twinkle_poem.txt')

b = a.read()

if 'Twinkle' in b:
    print('present')
else:
    print("not present")
# print(b)
a.close()