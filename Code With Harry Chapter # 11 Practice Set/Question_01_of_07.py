# Question # 01 

# Create a class of 2d vector from which inherit your 3d vector class 

class C2dvector:

    def __init__(self , i , j):
        self.icap = i 
        self.jcap = j 

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dvector(C2dvector):
    def __init__(self, i, j , k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

obj1 = C2dvector(4 , 7 )

obj2 = C3dvector(2 , 6 , 8)

# obj1.__str__()
# obj2.__str__()

print(obj1)
print(obj2)