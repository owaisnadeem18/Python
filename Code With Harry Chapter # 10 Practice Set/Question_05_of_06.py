# Question # 05 
# In this Question , we've to create a class of Train in which we've to store the important information of any train running under Pakistani Trains . These Important informations could be your train's name , seats capacity and fare information 

class Train:
    def __init__(self , name , fare , capacity):
        self.name = name
        self.fare = fare
        self.capacity = capacity

    def info_of_train(self):
        print(f"The name of this train is {self.name} ")
        print(f"The Seat Capacity of this train is {self.capacity} ")

    def fare_of_train(self):
        print(f"The Fare of this train is : {self.fare} Rs ")

    def book_seat(self):
        if(self.capacity>0):
            print(f"Your seat has been booked and your seat number is : {self.capacity}")
            self.capacity = self.capacity - 1 
        else:
            print("Your Seat can't be booked , because train is full ")

object = Train("Pakistan Express" , 2500 , 6)

object.info_of_train()
object.fare_of_train()
object.book_seat()
object.info_of_train()