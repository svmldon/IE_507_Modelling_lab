set N;	
var Set{N}, binary;	
var Vertex{N}, binary;	
param W{N,N}; 
maximize cut : sum{i in N}sum{j in N} W[i,j]*Set[i]*Vertex[j];

s.t. con1{i in N}: Set[i] + Vertex[i] = 1;
