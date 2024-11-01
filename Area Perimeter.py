# Area perimeter of shapes
# Author: Valiant Jamison
# Date: 10/30/2024
# Version: 1.0

# TODO:
    # this will calculate the area and perimeter of shape
running = ""
def retangle():
    while True:
        length = float(input("Enter the length of the rectangle: "))
        if length <= 0:
            print("Please enter a number more than 0")
            continue
        width = float(input("Enter the width of the rectangle: "))
        if width <= 0:
            print("Please enter a number more than 0")
            continue
        area = length * width
        perimeter = (length + width) * 2
        print(f"The area of the rectangle is {area} \nThe perimeter is {perimeter}")
        break

while running == "":
    AreaPerimeter = retangle() #this calls the function and stores the value in num_1
    # 1 is a square and 2 is retangle
    running = input("Press <enter> to continue or any key to stop")