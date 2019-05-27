# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:36:50 2017

@author: svmldon
"""
import math
import numpy as np
import statistics

def ex1fun(a,m):
    b=[]
    i=len(a)
    j=i/m
    temp=0
    bavg=0
    j=math.floor(j)
    for x in range (0,j):
        for y in range (0,m):
            temp+=a[m*x+y]
        b.append(temp/m)
        temp=0
    print ("Number of elements in vector=",len(b))
    print ("Maximum value of all elements in vector=",np.amax(b))
    print ("Minimum value of all elements in vector=",np.amin(b))
    for x in range (0,j):
        bavg+=b[x]
    bavg=(bavg/j)
    print ("Average value of all elements in vector=",bavg)
    print ("Standard deviation of all elements in vector=",statistics.stdev(b))
    
    import matplotlib.pyplot as plt
    
    plt.hist(b, bins='auto')  # arguments are passed to np.histogram
    plt.title("Histogram with 'auto' bins")
    plt.show()
    
    
        
    
    

m=int(input("Enter the value of m"))
a=[]
fname=open("ex1a")
fline=fname.readline()
while (fline):
    a.append(int(fline))
    fline=fname.readline()
    
ex1fun(a,m)


 
