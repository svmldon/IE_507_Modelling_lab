n=(readline(prompt="Enter the number of products: "))
qCheck=function(N){
  n=as.integer(N)
  rwrong=0
  rcorrect=0
  x=rnorm(n,mean=10,sd=0.2)
  #print(x)
  index=sample(n,0.3*n,replace=T)
  #print(index)
  for (i in index){
    if(x[i]>=9.6 && x[i]<=10.4)
    {rcorrect=rcorrect+1}
    else {rwrong=rwrong+1}
  }

  rcorrect1=rcorrect*0.999
  rwrong1=rwrong*0.95
  rcorrect2=rwrong-rwrong1
  R=rcorrect1+rcorrect2
  
  P1=R*.995
  P2=R*.005
  PC1=P1*.995
  PC2=(R-P1)*.01
  PCorrect=PC1+PC2
  
  print("fraction defective")
  print((n*.3-PCorrect)/n)
  wrong1=rwrong+P2
  print("wrong painted or radius wrong fraction")
  print(wrong1/n)
  rconew=rcorrect*(0.001)+R*(.005)
  print("had the right paint and radius right but consider as a defective ")
  print(rconew/n)
  
  
  
  
  
}
qCheck(n)