binomial=function(trail,n,p)
{
  
  x=rbinom(trail,n,p)
  return(x)
}

bernouli=function(trail,n,p)
{
  vec=c()
  for (i in 1:trail)
    {
    x=rbinom(n,1,p)
    sum1=sum(x)
    vec=append(vec,sum1)
  }
  return(vec)
  
}

n=as.integer(readline(prompt="Enter the value of n: "))
p=as.numeric(readline(prompt="Enter the value of p: "))
trail=as.integer(readline(prompt="Enter the number of trails: "))

hist((binomial(trail,n,p)),col='blue',main="n=1000,p=0.1")
hist((bernouli(trail,n,p)),col = 'red',main="n=1000,p=0.1")