n = int(input("Enter the number of rows:"))
c = int(input("Enter 1(normal) or 0(inverted):"))
c1 = bool(c)
row = 1
n1 = n
if c1:
    while(row <= n):
        itr = 1
        while(itr <= row):
            print("*", end="")
            itr += 1
        print()
        row += 1
else:
    while (row <= n):
        itr = 1
        while (itr <= n1):
            print("*", end="")
            itr += 1
        print()
        row += 1
        n1 -= 1