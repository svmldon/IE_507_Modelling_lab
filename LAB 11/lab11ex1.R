n=as.integer(readline(prompt="Enter the total no. of employees: "))


women=function(n){
pop=rbinom(n,1,0.4)
#print(pop)
index=sample(1:n, size=30, replace=TRUE)
#print(index)
count1=0
for(i in index){
  if (pop[i]==1)
  {count1=count1+1}
  }

return(count1)
 }
# To calcuate exact probablity
exact=(1-(0.6^30)-(0.4*0.6^29)-(0.4^2*0.6^28)-(0.4^3*0.6^27)-(0.4^4*0.6^26)-(0.4^5*0.6^25))
print("Exact probablity is : ")
print(exact)


# On the basis of random 1000 observations
count2=0
for(i in 1:1000){
  if(women(n)>5){
    count2=count2+1
  }
}
probx5=(count2/1000)
print("P[X>5] for 1000 observations")
print(probx5)