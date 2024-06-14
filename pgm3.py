#Assignment 1/pgm3

#Write a python program that calculates the factorial of a given number.

def fac():
    fac=1
    num=int(input("Enter a number:"))
    if (num<1):
        print("Number should be positive.")
    elif (num==0):
        print("Factorial is 1")
    elif (num>1):
        for i in range(1,num+1):
             fac=fac*i
        print("Factorial of the entered number is:",fac)
fac()