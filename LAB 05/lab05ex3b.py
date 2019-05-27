# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 01:22:02 2017

@author: svmldon
"""

a=int(input("Enter the number to be perfect or not to be found="))
sum=0
for i in range (1,a):
    if (a%i==0):
        sum+=i
if (sum==a):
    print ("Number is a perfect number")
else:
    print ("Number is not a perfect number")
    