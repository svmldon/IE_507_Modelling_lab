# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:38:43 2017

@author: svmldon
"""

import numpy as np
import random

def mat(m,n):
    A=[[random.randint(1,m) for j in range(n)] for i in range(m)]
    for i in range(0,m):
        maxcl=A[i][i]
        maxrow=i
        for k in range(i+1,m):
            if (A[k][i]>maxcl):
                maxcl=A[k][i]
                maxrow=k
                
        for k in range(i,n):
            tmp=A[maxrow][k]
            A[maxrow][k]=A[i][k]
            A[i][k]=tmp
        
        for k in range(i+1,m):
            c=((-1*A[k][i])/(A[i][i]))
            for j in range(i,n):
                if i==j:
                    A[k][j]=0
                else:
                    A[k][j]+=c*A[i][j]
    print (A)
    
    

m=int(input("Enter the number of rows of matrix:"))
n=int(input("Enter the number of columns of matrix:"))
mat(m,n)

