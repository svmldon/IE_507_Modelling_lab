# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 14:45:50 2017

@author: svmldon
"""
import numpy as np
import math
import matplotlib.pyplot as plt

def profitfun(stock,a):
    profit=[]
    for x in a:
        if (x>=stock):
            profit.append(6*stock)
        else:
            profit.append(x*6-2*(stock-x))
    averageProfit=sum(profit)/len(profit)
    return averageProfit

a=[]
fname=open("milk.txt")
fline=fname.readline()
while (fline):
    a.append(int(fline))
    fline=fname.readline()
    
print ("Mean of demand=",np.mean(a))
print ("Standard deviation of demand=",np.std(a))
plt.plot(a)
plt.show()
plt.hist(a)
plt.xlabel("Demand")
plt.ylabel("Frequency")
plt.show()

stock=int(input("Enter the value of stock you want to keep:"))
print("Profit Earned=",profitfun(stock,a))

xdemand=[]
xprofit=[]
for i in [500,600,700,800,900,1000,1100,1200,1300,1400,1500]:
    xdemand.append(i)
    xprofit.append(profitfun(i,a))
plt.plot(xdemand,xprofit)
plt.xlabel("quantity")
plt.ylabel("profit")
indexoptimum=xprofit.index(max(xprofit))
optimumStocks=xdemand[indexoptimum]
print("Stocks for maximum profit="+str(optimumStocks))
plt.show()
  