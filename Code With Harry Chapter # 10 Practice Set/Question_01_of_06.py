# Create a Class Programmer for storing information of some programmers working together in a Microsoft Company 

class Programmer:
    company = "Microsoft"
    def __init__(self , name , salary) :
        self.name = name 
        self.salary = salary 

    def getInfo(self):
        print(f"The name of the employee of {self.company} is {self.name} and his salary is {self.salary}")

owais = Programmer("Owais" , "80k")
hamza = Programmer("Hamza" , "50k")

owais.getInfo()
hamza.getInfo()