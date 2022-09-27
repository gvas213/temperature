import os
from os import system
system("clear")

# greeting
def greeting():
    name = input("Enter your name: ")
    print("Hello " + name + ".")

    return name

# temp input

def unites():
    unit = input("enter the unit, either farenheight (F) or celsius (C), that you would like to convert to.")
    unit = unit.upper()

    while unit != 'F' and unit != 'C':
        unit = input("enter the unit, either farenheight (F) or celsius (C), that you would like to convert to.")
        unit = unit.upper()

    return unit

def numbers():
    temp = input("Enter the temperature you'd like to convert.")

    while temp.isdigit() == False:
        temp = input("That is not number. Enter the temperature you'd like to convert.")

    temp = int(temp)
    return temp

# conversion
def conversions(x, y, z):
    
    if z == 'F':
        final_temp = ((x - 32)*(5/9))
        final_temp = str(final_temp)
        final_unit = "C"
        message = "Hi {}, {}{} is equivelent to {}{}.".format(y, x, z, final_temp, final_unit)    
        print(message)
    else:
        final_temp = (((x * 9)/5)+32)
        final_temp = str(final_temp)
        final_unit = "F"
        message = "Hi {}, {}{} is equivelent to {}{}.".format(y, x, z, final_temp, final_unit)
        print(message)

def game(x): 
    temp = numbers()
    unit = unites()
    conversions(temp, x, unit)
    question = input("Would you like to convert another temperature? Ifr so, press 'y'. Any other input will exit the program.")
    if question == "y":
        game(x)
    else:
        print("Bye.")

name = greeting()
game(name)



























# never leave your computer unattended