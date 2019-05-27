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
print(sum(resi))  #this should come to zero as residual=y-y` are distributed uniformly about the x axis`
plot(nico,resi, ylab="Residuals", xlab="Y") #if residuals are randomly scatted the linear regression is the best fit

print(model)
print(summary(model))

V=predict(model) #gives the estimated new values
print(V)
z=as.numeric(coef(model)) #stores the value of intercept and slope in array z
#to predict a new value for x will be given by
# y=z[1]+z[2]*x




