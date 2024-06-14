#Assignment 1/pgm20

#Write a python program that takes a list of numbers and returns their sum.

lst=[]

while True:
    nm=int(input("Enter a number:"))
    lst.append(nm)
    choice=input("Do you want to add a number again?")
    if (choice=='n'):
        break
print(lst)
sum_lst=sum(lst)
print("The sum of all the numbers present in the above list is:",sum_lst)