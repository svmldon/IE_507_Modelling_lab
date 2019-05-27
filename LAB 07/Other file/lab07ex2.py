import numpy as np
import matplotlib.pyplot as plt


def twodrand(n):
	x=np.random.uniform(0,1,n)
	y=np.random.uniform(0,1,n)
	plt.scatter(x,y)
	plt.show()
	plt.hist(x)
	plt.show()
	print (x)

n=int(input("Enter number of point to be gerneated"))
twodrand(n)
