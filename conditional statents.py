# Loops and indents
# Author: Valiant Jamison
# Date: 27/09/2024
# TODO:
# create a program that asks a user a qusetion
# and returns a response based on the answer on the screen
# Verison: 1.0

# Main loop. Keeps running unitl a condition is met
Keep_Going = ""
while Keep_Going == "":
    # asking the user for an input
    like_coffee = input("Do you like coffee?").lower()

    if like_coffee == "y" or like_coffee == "yes":
        print("i dont like coffee so you dont like coffee :) are you happy while i am not you dont like coffe noone likes coffee")

    elif like_coffee == "n" or like_coffee == "no":
        print("nice i also dont like coffee :)")

        like_tea = input("would you like tea instead?").upper()

        if like_tea == "Y" or like_coffee == "YES":
            print("meh tea mid")

        elif like_tea == "N" or like_coffee == "NO":
            print("THEN WHAT DO YOU LIKE :(")
            
    else:
        print("bruh i said yes or no try again")
        
    Keep_Going = input("Press <enter> to continue or any key to stop")