import random
l = ["r", "p", "s"]
def gamewinner(cc,uc):
    if uc == cc:
        return 0
    elif uc == "p" and cc == "r":
        return 1
    elif uc == "r" and cc == "s":
        return 1
    elif uc == "s" and cc == "p":
        return 1
    else:
        return 0

win = 0
for i in range(1,10):
    compchoice = random.choice(l)
    urchoice = input("Enter your choice(rock(r),paper(p),scissor(s)):")
    win += gamewinner(compchoice,urchoice)
print("The number of wins in best of 10 is ",win)