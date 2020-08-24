op = input("Enter the operation you want to perform:")
a = int(input("Enter the number1:"))
b = int(input("Enter the number2:"))
if op == "*":
    if a == 45 and b == 3:
        print("45 * 3 = 555")
    else:
        print(a, "*", b, "=", a*b)
elif op == "+":
    if a == 56 and b == 9:
        print("56 + 9 = 77")
    else:
        print(a, "+", b, "=", a+b)
elif op == "/":
    if a == 56 and b == 6:
        print("56/6 = 4")
    else:
        print(a, "/", b, "=", a/b)
else:
    print(a, "-", b, "=", a-b)