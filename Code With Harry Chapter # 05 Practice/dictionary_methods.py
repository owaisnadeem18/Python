
dictionary = {

"owais" : "a student" , 
"Fast"  : "a best Uni of Pakistan" ,
"List"  : [5 , 7 ,3 ] , 
"extra_dict" : {"owais" : "learner"} , 
56 : 23

}

dictionary["List"] = [9 , 42 , 68 ,25] 

print(dictionary["List"])

# Dictionary Methods 

print((dictionary.keys())) # Print the keys in a dictionary

print((dictionary.values())) # Print the values in a dictionary 

print((dictionary.items())) # Print (key , values) for all content of dictionary 

update_dict = {

    "Owais": "Loves to play cricket" ,
    "Ali Aslam": "A University Friend" , 
    "Atif Aslam": "A Pakistani Singer"

}

# print(update_dict)
# dictionary.update(update_dict)

# print(dictionary)

print(update_dict) 

dictionary.update(update_dict) # It will Update / Add more items in your dictionary  

# Similarities between them 
print(dictionary.get("Owais")) # Same Output will come
print(dictionary["Owais"]) # Same Output will come

# Differences between them 
print(dictionary.get("Owais1")) # It will throw none , as Owais1 is not present in the list .
# print(dictionary["Owais3"]) # It will throw an error 
