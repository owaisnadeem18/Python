# Multiple Inheritance
# In this inheritance , we use to say that if two or more thn two classes are combined to create only one class is called Multiple Inheritance

class father:
    name = "Nadeem"

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def show1(self):
        print(f"The name of the father is {self.name}")
        print(f"The Job of the father is {self.job}")


class mother:

    name = "Shahida"

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def show2(self):
        print(f"The name of the mother is {self.name}")
        print(f"The Job of the mother is {self.job}")


class son(father, mother):

    name = "Owais"

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def show3(self):

        print(f"The name of the son is {self.name}")
        print(f"The Job of the son is {self.job}")

        super().show1()
            # print("")


obj_father = father("Nadeem" , "Private Job")
obj_mother = mother("Shahida" , "House Wife")
obj_son = son("Owais" , "Uni Student")

obj_father.show1()
obj_mother.show2()
obj_son.show3()