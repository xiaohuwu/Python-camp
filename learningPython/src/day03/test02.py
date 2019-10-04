"""""
寻找“完美数”


"""""
for x in range(1,1001):
    array = []
    for item in range(1, x):
        if x % item == 0:
            array.append(item)
    if len(array) >= 2:
        sum = 0
        for y in array:
            sum += y
        if sum == x:
            print("item =", x)


