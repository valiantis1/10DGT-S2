# Error checking
# Author: Valiant Jamison
# Date: 2024/10/16
# Version: 1.0

#test if the number is valid
'''done = False
while not done:  #while loop that runs until

    num = int(input("please enter your value:  "))
    done = True

print(f"the number you enter was {num}")
'''
# Code that tests that a valid number is entered(v2)
'''
def test_int_num(question):
    done = False
    while not done:
        print(question)
        try: # this tries for a input
            num = int(input())
            done = True

        except ValueError:
            print("that is not a valid number")

    return(num) #give back the value of num
num_1 = test_int_num("Please enter you first number:")
print(f"You entered {num_1}.")

num_2 = test_int_num("Please enter you second number:")
print(f"You entered {num_2}.")

num_3 = test_int_num("Please enter you third number:")
print(f"You entered {num_3}.")

sum = num_1 + num_2 + num_3
print(f"The total of {num_1}, {num_2} and {num_3} is {sum}")
'''
# v3 make the code smaller
#ask the user to pick a number in a range
def valid_num(question, low, high):
    error = f"That is not a valid number. Please enter an integer between {low} and {high}"
    while True:
        try:
            response = int(input(question))
            if low < response < high:
                break
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)
    return(response)
num_1 = valid_num("Enter a number between 1 and 15: ", 1, 15,)
print(f"You entered {num_1}.")
