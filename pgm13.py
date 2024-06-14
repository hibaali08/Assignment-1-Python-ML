#Assignment 1/pgm13

#Write a program that asks the user for their birth year and calculates their age.

from datetime import date
#'datetime' is a built in module in python and 'date' is a function in it.
#we check if current month and date are less than birth month and date. If yes subtract 1 from age, otherwise 0 to calculate age precisely.
#The 'datetime' is already feeded with present-day date.

 
def agecalc(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
 
    return age
     
print(agecalc(date(2005,8,25)), "years")
