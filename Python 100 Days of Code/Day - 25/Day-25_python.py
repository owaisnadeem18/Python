# Operations On Tuples in Python 

tuple_operations = (4 , 8 , 2 , 9 , 8 , 1 , 31 , 8 , 4 , 3)

print(tuple_operations)
p = tuple_operations.count(4) # It Will Count The how many time respected Number available in our tuple
i = tuple_operations.index(4)
print("Count of 08 in tuple-operation is -> " , p)
print(i)

print(len(tuple_operations))

p1 = tuple_operations.index(3 , 5 , 8)
print(p1)