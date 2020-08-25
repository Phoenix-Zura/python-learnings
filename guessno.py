
n = 100
while True:
    inp = int(input("Enter the guess:"))
    if inp == 100:
        print("Congratulations!! yo guessed the number correct")
        break
    elif inp < 100:
        print("The guess is less")
        continue
    elif inp > 100:
        print("The guess is more")
        continue
