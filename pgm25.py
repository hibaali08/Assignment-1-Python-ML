#Assignment 1/pgm25

#Write a program that copies the contents of one text file to another.

import os

def main():
    f=open("demo.txt","r")
    f1=open("demo1.txt","w")
    text=f.readlines()

    for i in text:
        f1.write(i)
    print("Content copied successfully!")
    
    f.close()
    f1.close()
main()