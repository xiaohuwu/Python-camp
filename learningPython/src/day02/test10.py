"""
输出乘法口诀表(九九表)

Version: 0.1
Author: 骆昊
"""
from __future__ import print_function

for x in range(1,10):
    for y in range(1,x+1):
        print("{} * {} = {} \t".format(y, x, x * y), end='', flush=True)
    print()
