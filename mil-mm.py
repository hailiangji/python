# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 14:11:25 2022

@author: HailiangJi
"""
import  serial
mil =float(input("mil = "))
mm = mil*0.0254

print("{:.0f}mil = {:.4f}".format(mil,mm),"mm")

