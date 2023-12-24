# Question_06
# In this Question , we've to search and find out that either we can replace our self parameter with either any other number or not 

class Sample:

    def __init__(owais , name): # you may use any other parameter in place of your self parameter , but it is not considered as a good practice 
        owais.name = name 

obj = Sample("Owais")
print(obj.name) # This is an Instance Attribute 

obj.b = "Hamza"
print(obj.b) 