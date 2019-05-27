# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:38:43 2017

@author: svmldon
"""

import numpy as np
import random

def mat(m,n):
    random.seed(9001)
    B=[[random.randint(1,m) for j in range(n) ] for i in range(m)] 
    print (B) 
    A=[[0] * (n+1) for i in range(m)]
    for i in range(m):
        for j in range(n):
            A[i][j]=B[i][j]
        A[i][n]=(5*B[0][i]+2*B[1][i])
    print ("Augmented matrix",A) 
    n=n+1
    for i in range(0,m):
        maxcl=A[i][i]
        maxrow=i                         
        for k in range(i,m):
            if (A[k][i]>maxcl):
                maxcl=A[k][i]
                maxrow=k
                
        for k in range(i,min(m,n)):
            tmp=A[maxrow][k]
            A[maxrow][k]=A[i][k]
            A[i][k]=tmp
        for k in range(i+1,m):
            c=float((-1*A[k][i])/(A[i][i]))
            for j in range(i,n):
                if i==j:
                    A[k][j]=0
                else:
                    A[k][j]+=c*A[i][j]
    print ("Augmented matrix",A) 
    n=n-1
    count=0
    count1=0
    for i in range(0,m):
        count=0
        for j in range(0,n):
            if(A[i][j]==0.0):
                count+=1
        if(count==n):
            count1+=1
    rank=m-count1
    if(rank==m):
        print("Given column vectors are linearly independent")
    else:
        print("Given column vectors are linearly dependent")
                
    print("Rank of the matrix is",rank) 
    if (rank==n):
        print("Solvable:")
        x = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
            x[i] = A[i][n]/A[i][i]
            for k in range(n-1, -1, -1):
                A[i-1][n]-= A[i-1][k] * x[k]
        print ("Solution ",x)
    else:
        print("Not solvable as number of variables exceed no. of constraints")
    
    

def mat1(m,n):
    random.seed(9001)
    B=[[random.randint(1,m) for j in range(n) ] for i in range(m)] 
    print (B) 
    A=[[0] * (n+1) for i in range(m)]
    for i in range(m):
        for j in range(n):
            A[i][j]=B[i][j]
        A[i][n]=(5*B[0][i]+2*B[1][i])
    print ("Augmented matrix",A) 
    n=n+1
    for i in range(0,m):
        for j in range(i+1,m):
            for k in range(i,n):
                    A[j][k]=float(A[j][k]-((A[i][k]*A[j][i])/A[i][i]))
    count=0
    count1=0
    for i in range(0,m):
        count=0
        for j in range(0,n):
            if(A[i][j]==0.0):
                count+=1
        if(count==n):
            count1+=1
    rank=m-count1
    if(rank==m):
        print("Given column vectors are linearly independent")
    else:
        print("Given column vectors are linearly dependent")               
    print("Rank of the matrix is",rank)       
    print("Solvable:")
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(n-1, -1, -1):
            A[i-1][n]-= A[i-1][k] * x[k]
    print ("Solution ",x)
    
m=int(input("Enter the number of rows of matrix:"))
n=int(input("Enter the number of columns of matrix:"))
if (m<=n):
    mat(m,n)
else:
    mat1(m,n)

