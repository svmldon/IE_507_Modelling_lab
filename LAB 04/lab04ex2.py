print("Enter the positive integer number which is prime or not is to be found")
a=int(input("The number"))
if a> 1:
   for i in range(2,a):
       if (a % i) == 0:
           print("Entered number is not a prime number")
           break
   else:
      print("Entered numberis a prime number")      
else:
   print("Entered numberis not a prime number")
