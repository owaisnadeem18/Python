# Solve Question # 01 with while loop 

a = range(1,11)

b = 1
c = int(input("Enter A Number's Table = "))

while b<=10:
    # print(str(c) + "*" + str(b) + "=" + str(c*b))
    print(f'{c} X {b} = {c*b} ')
    b = b + 1 