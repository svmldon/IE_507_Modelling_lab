x=seq(50,5000)
y=sqrt(x)
z=x[y%%2==0]
print(z)

x=seq(50,5000)
y=x[((sqrt(x))%%2==0)]
print(y)
