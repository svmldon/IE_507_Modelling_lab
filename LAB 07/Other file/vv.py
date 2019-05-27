# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:11:42 2017

5@author: Ashu
"""
import numpy as np
def func(B,m,n):
     
    for i in range(min(m,n)):
         
        maximum = abs(B[i][i])
        maxRow = i
        for k in range(i+1, m):
            if abs(B[k][i]) > maximum:
                maximum = abs(B[k][i])
                maxRow = k

         
        for k in range(i,min(m,n)):
            y= B[maxRow][k]
            B[maxRow][k] = B[i][k]
            B[i][k] = y
            
        for k in range(i+1, m):
            c = (-B[k][i])/B[i][i]
            for j in range(i, n):
                if i == j:
                    B[k][j] = 0
                else:
                    B[k][j] += c * B[i][j]   
    print(B)

 
    r=0
    for i in range(min(m,n)):
        for  j in range (0,n):
            if B[i][j]!=0:
                r+=1
                break
    return r



# input command for no. of rows amd column for matrix.

r= int(input("Enter a no. of Rows"))
c= int(input("Enter a no. of Columns"))
A=np.random.randint(1, r+1, (r, c))
b=[]
b=A.sum(axis=1) # THE VALUE OF LEMDA IS TAKEN TO BE 1. SO b ELEMENT CAN BE SUM OF ALL THE ELEMENTS OF ROWS
print(b) 
print(A)



 



D=A.tolist() # this is used to change matrix into array
print(D)
for i in range(r):
    D[i].append(b[i]) # append the b into augmented matrix
D=np.array(D)
print(D)
e=func(A,r,c)
print("Rank of simple matrix is ",e)
if e<r:
    print("The column vectors are linear dependent")
else :
    print("The Column vectors are independent")

y=func(D ,r,c+1)
print(" Rank of augmented matrix is " , y)
if e==y & y==c:
   print(" The set of equation is solvable and unique solutions exists ")
elif e==y & y<c:
    print ("Multiple solution Exists" )
else:
    print(" No Solution exists")    
b=np.array(b)

x=np.linalg.solve(A,b)
print(x) 







    
 

    

    
    
    

    

    
    

   
    





