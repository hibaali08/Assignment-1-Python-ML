#Assignment 1/pgm24

#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
opt=input("Enter arithmetic operator (+,-,*,/):")

if (opt=='+'):
    print(num1+num2)
elif (opt=='-'):
    print(num1-num2)
elif (opt=='*'):
    print(num1*num2)
elif (opt=='/'):
    print(num1/num2)
else:
    print("Invalid operation!")