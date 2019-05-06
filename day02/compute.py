"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
"""
f = float(input("请输入华氏温度: "))
c = (f - 18) / 1.8
print("{:.1f} 华氏温度 = {:.1f} 摄氏温度".format(f, c))
