set.seed(1000000)
obs=rbinom(10000,35,0.45)
print(obs)
T=(sqrt(35)*((obs/35)-0.45))
print(T)
par(mfrow=c(2,2))
boxplot(T,main="Boxplot of Ti")
hist(T,breaks = 10)

y=c()
par=seq(0,1,0.01)
for (i in 1:100)
{a=log(10)
for (j in 1:1000)
{a=a+log((par[i]^obs[j])*((1-par[i])^(35-obs[j])))}
y[i]=a}
plot(y)
for (i in 1:100)
{if (max(y)==y[i])
{print(par[i])}
  }