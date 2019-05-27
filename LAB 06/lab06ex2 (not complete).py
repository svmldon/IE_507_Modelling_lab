# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 17:34:18 2017

@author: svmldon
"""

import numpy as np
import math
import matplotlib.pyplot as plt

a=[]
fname=open("tv.txt")
fline=fname.readline()
while (fline):
    a.append(int(fline))
    fline=fname.readline()

store=[]
store.append(int(5000))
warehouse=[]
warehouse.append(int(5000))
distribution=[]
distribution.append(int(5000))
assembly=[]
assembly.append(int(5000))
totalinvcost=0
bcost=0

for i in range(0,100):
	if (a[i]<=store[i]):
		store[i+1]=store[i]-x
		warehouse[i+1]=warehouse[i]
		distribution[i+1]=distribution[i]
		assembly[i+1]=assembly[i]
		totalinvcost=100*store[i+1]+80*warehouse[i+1]+60*distribution[i+1]+50*assembly[i+1]
		
	else:
		bcost=110*(a[i]-store[i])		
		store[i+1]=qty
		if (warehouse[i]>=qty):
			warehouse[i+1]=warehouse[i]-qty
		else:
			
		














		
	


    
