#Assignment 1/pgm12

#Write a python program that calculates the sum of the digits of a given number.

num=input("Enter a number:")
sum=0
for i in num:
    sum+=int(i)
print("The sum of the digits given in the entered number is:",sum)