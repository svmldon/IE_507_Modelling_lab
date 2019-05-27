n=readline(prompt="Enter the number of students: ")

simvirus=function(n)
{infected=c()
infected[1]=1 #assigning first effected computer of Bindu
v=sample(2:n,1) #first virus will infect computers of other than Bindu
print(v)
infected=append(infected,v)
i=2
 while(i>=2){
   v=sample(1:n,1)
   if (v==tail(infected,n=1)) #infected computer cannot infect itself it will infect other pcs
   { next}                  
   print(v)
   for (i in infected)   #if an infected pc choses to infect other pc which is already infected then no. of infected pcs returns
   {if (v==i){
     print(infected)
     return (length(infected))
   }
     }
   
   infected=append(infected,v) #new pc gets infected
   
 }

  
}
effected=simvirus(n)
print("Number of computers effected=")
print(effected)
n1=readline(prompt="Enter the number of simulation: ")
i=0
pceffect=c()
for (i in 1:n1) 
{pceffect=append(pceffect,simvirus(20))}
print("Mean number of computers effected:")
print(mean(pceffect))
print("Variance of computers effected:")
print(var(pceffect))
print("Number of runs:")
print(n1)
hist(pceffect)

