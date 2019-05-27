#first run the following single line to input the value of n

no=readline(prompt="Enter the number of variables: ")

#now run the following lines as a whole to get the result
n=seq(1,no)
xmean=c()
xmedian=c()
ymean=c()
ymedian=c()

for (i in n) {
  x=rnorm(i)
  xmean[i]=mean(x)
  xmedian[i]=median(x)
  y=rcauchy(i,location=0,scale=1)
  ymean[i]=mean(y)
  ymedian[i]=median(y)
}

par(mfrow=c(2,2))
plot(n,xmean,type='b',col='blue')
plot(n,ymean,type='b',col='red')
plot(n,xmedian,type='b',col='green')
plot(n,ymedian,type='b')