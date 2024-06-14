#Assignment 1/pgm16

#Write a program in python that counts the frequency of each character in a string.

def main():
    str1=input("Enter a string:")
    count={}
    for i in str1:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print("Frequency of each character entered in the above string is:",count)

main()