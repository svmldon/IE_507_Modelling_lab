# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:39:38 2017

@author: svmldon
"""

import random
import numpy
from math import floor, ceil
a=[0]*6
rand = float(0)
q = 0    
while q < 5000:
    q = q + 1
    rand = ceil(6*(random.random()))
    if rand == 1:    
        a[0]+= 1
    elif rand == 2:
        a[1]+= 1
    elif rand == 3:
        a[2]+= 1
    elif rand == 4:
        a[3]+= 1
    elif rand == 5:
        a[4]+= 1
    else:
        a[5]+= 1


for i in range (0,6):
    print(i+1," apears no. of times=",a[i])   
    
b=(1,2,3,4,5,6)
    
import matplotlib.pyplot as plt

plt.hist([b,a])  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()