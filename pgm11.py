#Assignment 1/pgm11

# Write a python program that generates the first n numbers in the Fibonacci sequence.

l=int(input("Enter nth number or limit:"))
n1=0
n2=1
cnt=0
if  (l<= 0):
   print("Please enter a positive integer")

elif  l== 1:
   print("Fibonacci sequence upto",l,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while cnt < l:
       print(n1)
       sum = n1 + n2
  
       n1 = n2
       n2 = sum
       cnt += 1