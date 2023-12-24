# Question # 02 
# Write a Program in which create a class name Animal and from which inherit 
# Another class of pet from it 

class animal:
    def __init__(self , walk , eat):
        self.walk = walk 
        self.eat = eat 

    def function(self):
        print(f"The Animal use to walk here ? {self.walk}")
        print(f"The Animal use to eat here ? {self.eat}")
    
class Pet(animal):

    def __init__(self, walk, eat):
        super().__init__(walk, eat)

class dog():

    @staticmethod
    def bark():
        print("Bow Bow !!!")

d = dog()
d.bark()

