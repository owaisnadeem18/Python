class Number:

    def __init__(self,num):
        self.num = num 

    def __add__(self , num2):
        print("Let's Add !!!")
        return self.num + num2.num

    def __mul__(self , num2):
        print("Let's Multiply !!!")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number = {self.num}"

    def __len__(self):
        return 5


# n1 = Number(7)
# n2 = Number(4)

n = Number(5)
print(n)
print(len(n))
# sum = n1 + n2 
# print(sum)
# multi = n1 * n2 
# print(multi)