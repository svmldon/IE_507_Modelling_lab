set.seed(1000000)
obs=rbinom(10000,35,0.45)
print(obs)
T=(sqrt(35)*((obs/35)-0.45))
print(T)
par(mfrow=c(2,2))
boxplot(T,main="Boxplot of Ti")
hist(T,xaxp  = c(-2, 2, 10))     #plot(..., xaxp  = c(x1, x2, n)) to 
#define the position (x1 & x2) of the extreme tick marks and 
#the number of intervals between the tick marks (n). 

y=c()
par=seq(0,1,0.01) #we will select value of p from this 0 to 1 increment 0.01
for (i in 1:100) # 100 times as par=seq(0,1,0.01) has 100 values
{a=log(10)
 for (j in 1:10000)
 {                                                   #for each value of p binomail 
   a=a+log((par[i]^obs[j])*((1-par[i])^(35-obs[j]))) #value is calculated for all values of observation
   }       #i.e p^x*(1-p)^(n-x) (see pdf for more details) and multiply all of them which is not possible 
 y[i]=a    #as p<1 raised to certain power ->0 so we had to take log value and then sum and check for what value 
 }         #value of p L(p,x) gives maximum value
plot(y)
for (i in 1:100)
{
   if (max(y)==y[i]) #if maximum value found then print that p
   {
     print(par[i])
     }
  }