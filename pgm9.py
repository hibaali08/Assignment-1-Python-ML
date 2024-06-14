#Assignment 1/pgm9

#Write a python program that checks if a substring is present in a given string.

str1=str(input("Enter a string:"))
str0=str(input("Enter a sub-string:"))
if (str0 in str1):
    print("Entered substring is present in the previously entered string.")
else:
    print("Entered substring is not present in the previously entered string.")