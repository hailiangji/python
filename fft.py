# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:57:26 2022

@author: HailiangJi
"""

import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np
from math import pi
plt.close("all")
#generate sine wave
Fs = 1000
t = np.arange(0,1,1/Fs)
f = 20
y=np.sin(2*pi*f*t)+0.8*np.sin(2*pi*200*t)+0.5*np.sin(2*pi*300*t)+0.3*np.sin(2*pi*400*t)+0.1*np.sin(2*pi*500*t)

print(type(y))
print(y)

plt.subplot(3,1,1)
plt.plot(t,y)
plt.title("sine signal")
plt.xlabel("time(s)")
plt.ylabel("Amplitude")

#compute fft
ff=fft(y)
print("len ff = ",len(ff))
n = np.size(t)

fr = np.linspace(0, 1,int(n))
print("np.size(fr)=",np.size(fr))

fft2 = abs(ff[0:np.size(fr)])
plt.subplot(3,1,2)
plt.plot(fr,fft2)

'''
fr = (Fs/2)*np.linspace(0, 1,int(n/2))
xff=abs(ff[0:np.size(fr)])
plt.subplot(3,1,3)
plt.plot(fr,xff)
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency(Hz)")
plt.ylabel("Magnitude")

'''
plt.tight_layout()