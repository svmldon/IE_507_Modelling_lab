param N;
set S:=1..N;
param SPRICE{S};
param LSIZE{S};
param ELEV{S};
var b0>=0;
var b1;
var b2;
var x{S};
minimize residual: sum{i in S}x[i];
c1{i in S}: SPRICE[i]-b0-b1*LSIZE[i]-b2*ELEV[i]>=-x[i];
c2{i in S}: SPRICE[i]-b0-b1*LSIZE[i]-b2*ELEV[i]<=x[i];