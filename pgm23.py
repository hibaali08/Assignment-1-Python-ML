#Assignment 1/pgm23

# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

def main():
    deg_cel=int(input("Enter temperature in degree celcius:"))
    temp_f= (deg_cel*1.8) + 32
    print(deg_cel,"Celcius is equivalent to",temp_f," Farenheit degree.")

    deg_fht=int(input("Enter temperature in degree farenheit:"))
    temp_c= (deg_fht-32)/1.8
    print(deg_fht,"Farenheit is equivalent to",temp_c,"Celcius degree.")

main()