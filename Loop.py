# Loops and indents
# Author: Valiant Jamison
# Date: 20/09/2024
# Verison: 1.0
# TODO:
    # idk

num1 = int(input("whats your name? "))
num2 = int(input("whats your fav color? "))
stuff = num1 + num2
print(f"your name is {num1} and you fav color is {num2}")


# for loops. Repeat for a set number of times.
# for start the loop
# next is name of the loop
# in range tells the loop how many times to run
# the number in the () is how many times it repeats
for name_of_loop in range(5):
    print("ha!")

# while loop. Runs until a condition is met
keep_going = " "
while keep_going == "":
    print("hi")
    print("still going")

    keep_going = input("again? or press any other key to quit")