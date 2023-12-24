
# Write a Program in which convert Hindi Written Words into English

new_dictionary = {

    "ghadi"  : "Watch" , 
    "pankha" : "Fan"  , 
    "bhai"   : "Brother" , 
    "maa"    : "Mother" 

} 

print("Options are : " , new_dictionary.keys())

v = (input("Enter an Urdu word : "))

print("The result of your search is : " , new_dictionary.get(v))  

