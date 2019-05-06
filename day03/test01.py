"""
水仙花数
"""
import math

for x in range(100,1000):
    bai = int(x / 100)
    sheng = x % 100
    shi = int(sheng / 10)
    ge = x % 10
    if (math.pow(bai, 3) + math.pow(shi, 3) + math.pow(ge, 3)) == x:
        print("x = {}".format(x))
