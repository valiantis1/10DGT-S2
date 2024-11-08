# Fence Costs
# Author: Valiant Jamison
# Date: 11/6/2024
# Version: 1.0

# TODO:
    # this will calculate the area and perimeter of shape
running = ""

def FenceLength():
    while True:
        try:
            length = float(input("Enter the length of the fence in meters: "))
        except ValueError:
            print("Please enter a number more than 0")
            continue
        
        if length <= 0:
            print("Please enter a number more than 0")
        else:
            return(length)

def FenceWidth():
    while True:
        try:
            width = float(input("Enter the width of the fence in meters: "))
        except ValueError:
            print("Please enter a number more than 0")
            continue

        if width <= 0:
            print("Please enter a number more than 0")
        else:
            return(width)

def FencePrice():
    while True:
        try:
            price = float(input("Enter the price per meter: $"))
        except ValueError:
            print("Please enter a number more than 0")
            continue
        
        if price <= 0:
            print("Please enter a number more than 0")
        else:
            return(price)

while running == "":
    Length = FenceLength() #this calls the function and stores it
    Width = FenceWidth() #this calls the function and stores it
    Price = FencePrice() #this calls the function and stores it
    Perimeter = (Length + Width) * 2 #This finds the perimeter
    Perimeter = round(Perimeter, 2) #This rounds the perimeter to two decimal points
    Price = Perimeter * Price #This finds the price of the fence
    Price = round(Price, 2) #This rounds the price because money can only be two decimal points
    print(f"\nThe perimeter is {Perimeter} meters \nThe price per meter is ${Price}")
    running = input("Press <enter> to continue or any key to stop") #asks if the user wants to find the price of a different fence