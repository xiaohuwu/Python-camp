from random import randint

# 设定参数的默认值
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

# 可变参数
def add(*args):
   total = 0
   for val in args:
       total += val
   return total

print("总点数为:",roll_dice())
print("总点数为:",roll_dice(3))
print(add())
print(add(4,5,6))