# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:50:25 2017

@author: svmldon
"""

import random
from math import floor, ceil
a[6]
b[6]
c[6]
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
    print(i+1," in first dice apears no. of times=",a[i])
    
while q < 5000:
    q = q + 1
    rand = ceil(6*(random.random()))
    if rand == 1:    
        b[0]+= 1
    elif rand == 2:
        b[1]+= 1
    elif rand == 3:
        b[2]+= 1
    elif rand == 4:
        b[3]+= 1
    elif rand == 5:
        b[4]+= 1
    else:
        b[5]+= 1
        
for i in range (0,6):
    print(i+1," in second dice apears no. of times=",a[i])
        
for i in range (0,6):
    c[i]=a[i]+b[i]
    
for i in range (0,6):
    print(i+1," in second dice apears no. of times=",a[i])
        
    

        
        
        
        
        
        
        
        