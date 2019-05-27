nico = c(0.89,1.06,2.03,0.67,0.4,1.04,0.76,0.95,1.12,1.02,1.01,0.9)
co = c(13.6,16.6,23.5,10.2,5.4,15,9,12.3,16.3,15.4,13,14.4)

par(mfrow = c(1,2))
plot(nico,co,
     xlab = "Nicotine(mg)",
     ylab = "CO(mg)",
     main = "nicotine(X) vs carbon monoxide(CO) emission(Y )"
)

model=lm(co~nico)
resi = resid(model)
print(resi)
plot(co,resi, ylab="Residuals", xlab="Y") 
print(model)
print(summary(model))


Yes=c()
for (i in nico){
  Y2=10.96*i+2.929
  Yes=append(Yes,Y2)
}


V=data.frame(nico,Yes)
print("Yes=estimated new value")
print(V)

