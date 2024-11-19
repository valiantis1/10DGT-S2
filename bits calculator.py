# bit calculator
# Author: Valiant Jamison
# Date: 11/13/2024
# Version: 1.0

# TODO:
    # this will calculate the bits of a number, text and image


def decoration(sides, text):
    print(sides * 5 + " " + text + " " + sides * 5) #this will print the decoration

def Integer():
    while True:
        try:
            Integer = int(input("Enter a Integer: "))
            if Integer <= 0: #this will check if the number is positive
                print("Please enter a positive number")
                continue 
            Integer = bin(Integer)[2:] #this will convert the number to binary and rounds it by removing the first two characters
        except ValueError:
            print("Please enter a valid number")
            continue
        return Integer

def Text():
    while True:
        try:  
            text = len(str(input("Enter some text: ")))
            text = text * 8 #this will convert the text to bits
        except ValueError:
            print("Please enter a valid text")
            continue
        return text

def Image():
    while True:
        try:

            Width = int(input("Enter the width of your image: "))
            Height = int(input("Enter the hight of your image: "))
            if Width <= 0 or Height <= 0: #this will check if the number is positive
                print("Please enter a positive number")
                continue
            bits = Width * Height * 24 #this will calculate the bits of the image
        except ValueError:
            print("Please enter a valid number")
            continue
        return bits

running = ""
Instructions = input("Press <enter> to see the instructions or any key to continue. ") #this will ask the user if they want to see the instructions
if (Instructions == ""):
    decoration("-", "Instructions") #this will print the decoration
    print("This program will calculate the bits of a number, text and image.")
    print("You will be asked to enter a number, text and image.")
while running == "":
    WhatBit = input(f"\nWhat would you like to calculate the bits of? (Integer, Text, Image): ")
    WhatBit = WhatBit.upper()
    if (WhatBit == "INTERGER" or WhatBit == "I" or WhatBit == "INT"):
        print("You chose integer")
        IntegerInput = Integer()
        print(f"\nThe bits of the integer is {IntegerInput}")
        print(f"\nThe number of bits needed is {len(IntegerInput)}") #this will print the number of bits needed by get the length of the integer
    elif (WhatBit == "TEXT" or WhatBit == "T" or WhatBit == "TXT"):
        print("You chose text")
        text = Text()
        print(f"\nThe number of bits needed is {text}")

    elif (WhatBit == "IMAGE" or WhatBit == "P" or WhatBit == "IMG"):
        print("You chose image")
        Bits = Image()
        print(f"\nThe number of bis needed is {Bits}")
    else:
        print("Sorry, please choose integer, text or image") #this will print if the user enters a wrong input
        continue