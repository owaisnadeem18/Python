# Concept Of Tuples in Python 

tuple = (4 , 8 , 3)
# tuple[1] = 6 You can't ever change the value of a tuple , because it's unchangable in every case 

# Note : lists are changable , but tuples are fixed values

print(type(tuple) , tuple)

print(len(tuple))

print(tuple[2:3])
print(tuple[1:3])
print(tuple[-2:-3])
print(tuple[1:0])
print(tuple[-3:3])

if 67 in tuple:
    print("Yeah")
else:
    print("Sorry")