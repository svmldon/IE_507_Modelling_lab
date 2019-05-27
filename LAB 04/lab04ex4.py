import numpy as np
m=0
v=0
n=int(input("Enter number of numbers to be randombly gerneated"))
x=np.random.uniform(0,1,n)
for i in range (0,n):
    m=m+x[i]
    
m=m/n

for i in range (0,n):
    v=v+(x[i]-m)**2

v=v/n

print("Mean=",m,"Variance",v)    