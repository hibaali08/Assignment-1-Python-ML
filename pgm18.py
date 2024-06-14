#Assignment 1/pgm18

# Write a python program that checks if two strings are anagrams of each other.

str1=input("Enter first string:")
str2=input("Enter second string:")

count=0
for i in str1:
    if i in str2:
        count+=1
    else:
        print("Entered strings are'nt anagrams of each other.")
if count==len(str1)==len(str2):
    print("Entered strings are anagrams.")