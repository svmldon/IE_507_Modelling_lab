param N;
set location := 1..N;
set facility := 1..N;
param cost{facility,location};
var position{facility,location}>=0;

minimize Cost: sum {i in facility, j in location} cost[i,j]*position[i,j];
s.t. Supply{i in facility}: sum {j in location} position[i,j] = 1;
s.t. Demand{j in location}: sum {i in facility} position[i,j] = 1;
