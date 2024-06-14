#Assignment 1/pgm21

#Write a python program that counts the occurrences of a specific element in a list.

def main(lst,x):
    count=0

    for i in lst:
        count+=i.count(x)
    
    print(x,"occures",count,"times in the given list.")


main(lst=['ashiya','anusha','ananya','hiba'], x='a')  