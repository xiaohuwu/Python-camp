"""
用for循环实现1~100求和

Version: 0.1
Author: 骆昊
"""

sum = 0
for x in range(2,101,2):
    if x % 2 ==0:
      print("x:", x)
      sum += x
print("sum = {}".format(sum))
