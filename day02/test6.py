from random import randint

face = randint(1,6)
if face == 1:
    result = '唱歌'
elif face == 2:
    result = '跳舞'
elif face == 3:
    result = "学狗叫"
else:
    result = "倒霉孩子"

print(result)