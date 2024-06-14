#Assignment 1/pgm14

#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

def main():
    lines=[]
    while True:
        line=str(input("Enter a String"))
        if line:
            lines.append(line)
        else:
            break
    text='\n' .join(lines)
    print(text)
main()