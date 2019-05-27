set Alloy;
set Metal;
param QMAX;
param Pcent{Metal,Alloy};
param TMetal{Metal};
param H_Stock{Alloy};
param H_Cost{Alloy};
param P_Cost{Alloy};
var X{Alloy}>=0;
var Y{Alloy}>=0;
var Z{Alloy}>=0;

minimize Total_Cost:sum{j in Alloy} (Y[j]*P_Cost[j]+Z[j]*H_Cost[j]);
c1{i in Metal}:sum{j in Alloy} X[j]*Pcent[i,j]=TMetal[i];
c2:sum{j in Alloy} X[j]=QMAX;
c3{j in Alloy}: X[j]=Y[j]+Z[j];
c4{j in Alloy}: Z[j]<=H_Stock[j];

