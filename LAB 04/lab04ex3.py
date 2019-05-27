print ("please enter an array of 5 elements")
x1=float(input("1st number"))
x2=float(input("2nd number"))
x3=float(input("3rd number"))
x4=float(input("4th number"))
x5=float(input("5th number"))
list1=[x1,x2,x3,x4,x5]
for i in range(0,5):
    for j in range(0,5):
       if (list1[i]>list1[j]):
        temp=list1[i]
        list1[i]=list1[j]
        list1[j]=temp
print (list1)
