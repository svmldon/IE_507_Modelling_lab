import random 
import numpy as np
random.seed(100)



def Guass():
    x=input("do you want input matrix if yes then press 1 otherwise 0")
    if x==1:
        m=input("enter the no. of row")
        n=input("enter the no, of column")
        s=[]
        A=[]
        print ("input all elements of matrix start from 1st row to last row in order ")
        for i in range (0,m):
            for j in range (0,n):
                 
                x1 = float(raw_input(""))
                
                s.append(x1)
            A.append(s)
            s=[]
        A=np.array(A)
        print (A)
        
    else:
        m=input("enter the no. of row")
        n=input("enter the no, of column")
        emp=[]
        A=np.random.randint(1,m+1,(m,n)).astype('float')
        print A
    R= 0    
    for i in range (0,n-1):
        if A[i,i]!=0:
            
            for j in range (i+1,m):
                coff=A[j,i]/float (A[i,i])
                for k in range (i,n):
                    A[j,k]=A[j,k]-(A[i,k]*coff)
        elif A[i,i]==0:
            for p in range (i+1,m):
                if A[p,i]!=0:
                    
                    for j in range (0,n):
                        emp.append(A[i,j])
                        A[i,j]=A[p,j]
                        A[p,j]=emp[j]
                        break
                    for k in range (i,n):
                        A[j,k]=A[j,k]-(A[i,k]*coff)
    for f in range (0,m):
        for e in range (0,n):
            if e==f:
                
                if A[f,e] != 0:
                    R=R+1
                    break
                else:
                    continue
            else:
                continue
                
    print A
    print ("rank of matrix",R)


Guass()


