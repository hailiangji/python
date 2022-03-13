# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 23:02:12 2022

@author: HailiangJi
"""
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np
from math import pi

file =r"E:\WORK\_Sigtrum\__Board\Momhilsar\fab2\HW debug\ENOB_DC\10MHz-224Msps.txt" #224Msps

with open(file ,"r" ) as f:
    b=f.read()
    #a=np.array(b)
    print(type(file))
    Fs = int(224e6)
    Flen=65536
    tt=np.loadtxt(file)
    print("len tt = ",len(tt))
    print("max sine= ",max(tt))
    print("min sine= ",min(tt) )
    plt.subplot(3,1,1)
    x = np.linspace(0,len(tt)/Fs,len(tt))
    plt.plot(x[0:100],tt[0:100],color="green")
    plt.xlabel("time(s)")
    plt.ylabel("Amplitute")
    xx=fft(tt)
    

    np.set_printoptions(threshold=np.inf)
    cc = abs(xx)
    print("arg max frequnency={}MHz".format(np.argmax(xx)*224e6/Flen/1e6))
    DC = abs(xx[0])
    print("dc",xx[0])
    print("DC value = ",DC/Flen)
    print("max - min ",abs(max((tt))+min((tt)))/2)
    print("min",min((tt)))
    print("max",max(tt))
    
    y=np.linspace(0,Fs,Flen)
    plt.subplot(3,1,2)
    plt.plot(y,abs(xx)/Flen)
    #print("y=",y)

    print("lenth fft = ",len(xx))
    plt.tight_layout()
    
'''
    plt.subplot(3,1,3)
    plt.plot(abs(xx))
    plt.show()
    plt.tight_layout()
    #print(a)
'''    
    #print(y)
       #ffta=fft(a)
    #plt.plot(y,ffta)
    #plt.show()
'''   
    #print(a)
    print("type a",type(a))
    for i in a:
        print(i)
    #n = int(power(2, ceil(log2(len(a)))))
    #ff=fft(np.float64(a))
    fr=1/250e6
    print("fr",fr)
    print(type(fr))    
'''

    
    #plt.subplot(3,1,1)
    #plt.plot(xx,ff)
    
'''
    for i in f:
        print(i)
        print(type(i))
'''