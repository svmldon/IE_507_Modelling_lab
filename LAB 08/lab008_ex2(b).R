x=seq(0,1,0.05)
y=(1/exp(x))*cos(6*pi*x)
y1= exp(-x)

plot(x,y,type = 'b')
lines(x,y1,col='red')
lines(x,-y1,col='green')