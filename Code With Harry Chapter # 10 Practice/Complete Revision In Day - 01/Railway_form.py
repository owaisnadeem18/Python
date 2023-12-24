class RailwaysForm: # We've created a class with this format .  CLASS(class_name): 
    FormType = "Railway_Reservation_Form" # Just write it as an extra thing for my own covenience 
    def print_data(self): # Here , we'll create a function with any name like {function_name(def)}
        print(f"The name of passenger is {self.name}") # Here , we'll print the content which will be present in it 
        print(f"The name of passenger's Train is {self.train}") # # Here , we'll print the content which will be present in it 

YoursApplication = RailwaysForm() # We've (YoursApplication) as our object . Now , object = class()
YoursApplication.train = "Shalimar Express" # object.train means we are initializing our class attributes with the help of our object 
YoursApplication.name = "Owais" # object.name means we are initializing our class attributes with the help of our object

YoursApplication.print_data() # With the help of our {obj.function} we'll our class attributes