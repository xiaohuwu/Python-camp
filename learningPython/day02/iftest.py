"""
用户身份验证

Version: 0.1
Author: 骆昊
"""
while True:
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username =="admin" and password == "123456":
        print("success")
        break