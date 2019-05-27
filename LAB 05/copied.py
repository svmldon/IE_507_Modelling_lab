# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:39:38 2017

@author: svmldon
"""

import random
from math import floor, ceil
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
rand = float(0)
q = 0    
while q < 5000:
    q = q + 1
    rand = ceil(6*(random.random()))
    if rand == 1:    
        one = one + 1
    elif rand == 2:
        two = two + 1
    elif rand == 3:
        three = three + 1
    elif rand == 4:
        four = four + 1
    elif rand == 5:
        five = five + 1
    else:
        six = six + 1

total = one + two + three + four + five + six

print("1 apears no. of times=", one)    
print("2 apears no. of times=", two)
print("3 apears no. of times=", three)
print("4 apears no. of times=", four)
print("5 apears no. of times=", five)    
print("6 apears no. of times=", six)