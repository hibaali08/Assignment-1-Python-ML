#Assignment 1/pgm26

#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

def main():
    user_str=input("Enter a string:")


    result=user_str.startswith('a')
    print(result)
    if result==True:
        print("String starts with the given prefix 'a',")
    else:
        print("String does not start with the given prefix 'a'.")

    
    result=user_str.endswith('l' or 'L')
    print(result)
    if result==True:
        print("String ends with the given suffix 'l'.")
    else:
        print("String does not end with the given suffix 'l'.")
main()

#Let string= 'ananya is a good girl.' (copy to execute desired result.)