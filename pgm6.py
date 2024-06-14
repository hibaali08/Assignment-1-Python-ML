#Assignment 1/pgm6

#Write a program that reads the content of a text file and prints it to the console.

def main():
    f=open("demo.txt","r")
    lines=f.readlines()
    print("Text encountered in the file is as follows:",lines)
main()