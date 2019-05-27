n=seq(1,1000)
meannormal=c()
meancauchy=c()
mediannormal=c()
mediancauchy1=c()

for (i in n)
{
  normal=rnorm(i, mean = 0, sd = 1)
  cauchy=rcauchy(i, location = 0, scale = 1)
 meannormal[i]=mean(normal)
 meancauchy[i]=mean(cauchy)
 mediancauchy1[i]=median(cauchy)
 mediannormal[i]=median(normal)
} 
meannormal
meancauchy
par(mfrow=c(2,2))
plot(n,meannormal,type='b',col='red')
plot(n,meancauchy,type='b',col='blue')
plot(n,mediancauchy1,type='b',col='green')
plot(n,mediannormal,type='b')