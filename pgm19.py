#Assignment 1/pgm19

#Write a python program that removes all punctuation from a given string.

user_str=input("Enter a string:")
punc='''!()-[]{};:'"\,<>./?@#$%^&*__~'''
new_str = user_str

for i in user_str:
    if i in punc:
        new_str=new_str.replace(i,'')

print("Orignal string:",user_str)
print("Modified string:",new_str)