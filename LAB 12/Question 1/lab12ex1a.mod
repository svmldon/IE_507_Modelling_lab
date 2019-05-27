param N;
set S := 1..N;
param x{S};
param y{S};
param z{S};
param w{S};
var a>=0;
var b>=0;
var c>=0;
minimize cost:sum{i in S} w[i]*sqrt((a-x[i])^2+(b-y[i])^2+(c-z[i])^2);
