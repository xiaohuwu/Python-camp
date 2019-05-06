"""
输入M和N计算C(M,N)
"""
def funci(n):
    result = 1
    for n in range(1, n + 1):
        result *= n
    return result
m = int(input('m = '))
n = int(input('n = '))
print(funci(m) // funci(n)//funci(m-n))
