# -*- coding: UTF-8 -*-
"""
File name:    ss.py
Author:       HailiangJi
IDE:          PyCharm
Created time: 2022.03.14 12:26
"""
while True :
    try:
        a = int(input('请输入第一个整数:' ))
        b = int(input('请输入第二个整数:'))
        c = int(input('请输入第三个整数:'))
        if a>b and a>c :
            print(a)
        elif b>a and b>c :
            print(b)
        elif c>a and c>b :
            print(c)
    finally:
        print("sb")
