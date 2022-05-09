# -*- coding: UTF-8 -*-
"""
File name:    xiaodanchun.py
Author:       HailiangJi
IDE:          PyCharm
Created time: 2022.04.21 23:31
"""


m=eval(input())
i=0
sum=0
while (1+i)*i/2 <=m :
    i=i+1
    sum=sum+i
print('sum=',sum-i)
