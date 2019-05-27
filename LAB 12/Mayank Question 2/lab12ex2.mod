param N;
set facility:=1..N;
set location:=1..N;
param cost{facility,location};
var Trans{facility,location} integer >= 0;

minimize Total_Cost: sum {i in facility, j in location} cost[i,j] * Trans[i,j];
s.t. Supply{i in facility}: sum {j in location} Trans[i,j] = 1;
s.t. Demand{j in location}: sum {i in facility} Trans[i,j] = 1;

