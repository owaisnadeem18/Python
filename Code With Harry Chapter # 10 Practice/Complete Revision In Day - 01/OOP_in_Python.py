class A:
    def sum(self):
        return self.a + self.b 

Z = A()
Z.a = 45
Z.b = 55

Y = Z.sum()

print(Y) 