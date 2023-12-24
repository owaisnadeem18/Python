# ##  This is the way to enter and print an empty set in your computer #
# b = set()
# print(type(b))

# ## If u wanna add some different numbers in your empty set , then : 
# b.add(56)
# # b.add(67)
# # b.add(35)
# # b.add(92) 
# # b.add(92)  #Adding a value in a set more than once , does not create changes in a set .
# b.add((7 , 4 , 18 , 68 , 59))
# ##  b.add({3 , 5 , 7}) You cannot add lists and dictionaries in a set 

# b.clear()

# print(b)

# print(b)

# print(len(b)) ## To print length of a set , this set method will use .

# ## Removal of an Item 

# b.remove(56) ##It will remove 56 from the sets 
# ## b.remove(4) It wil throw an error , because 4 is not present in the list of sets
# print(b) 

# print(b.pop())


d = {5 , 25 , 52 , 71 , 69 , 53 , 59}
c = {5 , 87 , 23 , 61 , 74 , 82 , 36} 

e = d.intersection(c)#{5 , 25 , 52 , 71 , 69 , 53 , 59} , {5 , 87 , 23 , 61 , 74 , 82 , 36})

print(e)