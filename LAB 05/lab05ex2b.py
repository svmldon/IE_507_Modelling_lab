# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:45:21 2017

@author: svmldon
"""

import random
from math import floor, ceil
a=[]*12
rand = float(0)
q = 0    
while q < 5000:
    q = q + 1
    rand = ceil(12*(random.random()))
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
    elif rand == 6:
        a[5]+= 1
    elif rand == 7:
        a[6]+= 1
    elif rand == 8:
        a[7]+= 1
    elif rand == 9:
        a[8]+= 1
    elif rand == 10:
        a[9]+= 1
    elif rand == 11:
        a[10]+= 1
    else:
        a[11]+= 1


for i in range (0,12):
    print(i+1," apears no. of times=",a[i])   
    
b=(1,2.3,4,5,6,7,8,9,10,11,12)
    
import matplotlib.pyplot as plt

plt.hist(a,b)  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()
