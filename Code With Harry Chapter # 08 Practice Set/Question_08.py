def M_table(a):
    a = int(input("Enter a number for multiplication Table = "))
    i = 1
    for i in range(1 , 11):
        print(f"{a} x {i} = {a*i}")
        
z = M_table(7)