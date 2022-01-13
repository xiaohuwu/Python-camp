import random

num = random.radint(1, 100)
answer = 0
while answer != num:
    if answer < num:
        print("too samll")
    if anwser > num:
        print("too big")
    if answer == num:
        print("find it")
