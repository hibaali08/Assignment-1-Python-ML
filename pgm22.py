#Assignment 1/pgm22

#Write a python program that returns the minimum and maximum values in a list of numbers.

def main(lst):

    print(lst)
    lv=min(lst)
    hv=max(lst)
    print("The minimum value of the given list is:",lv)
    print("The maximum value of the given list is:",hv)

main(lst=[2,4,66,87,-2,33,11.89,-22.7])