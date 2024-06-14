#Assignment 1/pgm5

#Write a program that takes a string input from the user and writes it to a text file.

def main():
    f=open("demo.txt","w")

    while True:
        txt=str(input("Enter text:"))
        f.write(txt + '\n')
        ch=input("Do you want to continue writing?  (y/n)")
        if (ch=='n'):
            break
    print("Text written successfully!)")
    f.close()
main()