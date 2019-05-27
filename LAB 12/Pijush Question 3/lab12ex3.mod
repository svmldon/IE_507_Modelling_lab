set N;	#set N is the vertices
var S{N}, binary;	#S[i] gives the nodess which are in set s
var V{N}, binary;	#V[i] gives the nodess which are in set v

param W{N,N}; #W is the weight from edge

maximize cut : sum{i in N,j in N} W[i,j]*S[i]*V[j];

s.t. con1{i in N}: S[i] + V[i] = 1;
