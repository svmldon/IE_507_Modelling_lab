param x1=0.5;
param y1=0;
param z1=0;
param x2=10;
param y2=10;
param z2=0;
param x3=0;
param y3=0;
param z3=0.5;
param x4=2;
param y4=10;
param z4=0;
param x5=3;
param y5=0;
param z5=15;
param x6=8;
param y6=0;
param z6=2;
param x7=0;
param y7=12;
param z7=0;
param w1=5;
param w2=10;
param w3=7;
param w4=9;
param w5=3;
param w6=2;
param w7=2;
var x>=0;
var y>=0;
var z>=0;
minimize cost:w1*sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1)+(z-z1)*(z-z1))+
w2*sqrt((x-x2)*(x-x2)+(y-y2)*(y-y2)+(z-z2)*(z-z2))+
w3*sqrt((x-x3)*(x-x3)+(y-y3)*(y-y3)+(z-z3)*(z-z3))+
w4*sqrt((x-x4)*(x-x4)+(y-y4)*(y-y4)+(z-z4)*(z-z4))+
w5*sqrt((x-x5)*(x-x5)+(y-y5)*(y-y5)+(z-z5)*(z-z5))+
w6*sqrt((x-x6)*(x-x6)+(y-y6)*(y-y6)+(z-z6)*(z-z6))+
w7*sqrt((x-x7)*(x-x7)+(y-y7)*(y-y7)+(z-z7)*(z-z7))
