class student():
    def __init__(self , name , clas) :
        self.name = name
        self.clas = clas

    def info(self):
        print(f"The name of the student is {self.name} ")
        print(f"The class of the student is {self.clas} ")

class son(student):
    
    number = "4th"

    def __init__(self, name , clas):
        self.name = name
        self.clas = clas

    def info_of_son(self):
        print(f"The respect % of this son is : {self.name} ")
        print(f"The marks of this son are : {self.clas} ")

obj1 = student("Owais" , "3rd Year")
obj2 = son("80%" , 90)
# obj2 = son()

obj1.info()

obj2.info()

obj2.info_of_son()