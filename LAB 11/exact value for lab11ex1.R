value=0
for(i in 0:5){
  value=value+((choose(30,0)*0.4^i*0.6^(30-i)))
}
print(1-value)