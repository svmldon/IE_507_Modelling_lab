# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:38:43 2017

@author: svmldon
"""

import numpy as np
import random

def mat(m,n):
    A=[[random.randint(1,m) for j in range(n)] for i in range(m)]
    A=[[1,2,2,2],[2,4,6,8],[3,6,8,10]]
    print (A)
    for i in range(0,m):
        for j in range(i+1,m):
            for k in range(0,n):
                    A[j][k]=A[j][k]-((A[i][k]*A[j][i])/A[i][i])
    print (A)
            
    
    
    

m=int(input("Enter the number of rows of matrix:"))
n=int(input("Enter the number of columns of matrix:"))
mat(m,n)

