import math 
print ("Enter values of a,b,c for qudratic equation ax^2+bx+c=0")
a=float(input("Enter value of a"))
b=float(input("Enter value of b"))
c=float(input("Enter value of c"))
d=(b*b-4*a*c)
if (d<0):
   print ("Cannot find a solution")
   quit()
x=((-b+math.sqrt(b*b-4*a*c))/(2*a))
y=((-b-math.sqrt(b*b-4*a*c))/(2*a))
print("\n Roots of the equation are",x,"and",y)
