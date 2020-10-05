"""

Program: get_user_input.py

Author: Donald Butters

Last date modified: 10/5/2020

The purpose of this program is prompt a name, age, and hourly pay.
Then the program out prints the input as a string

"""

def get_user_input(): # keyword def with function name then ():
    """Prompts the user for name, age and prints a message"""  # docstring
    name = input("Please enter your name:")  # user input string
    age = int(input('Please enter your age. :')) # user input int
    if age in range(1,120): # handle the bad
        print("Thank you")
    else:
        input("Please enter your age between 1-120. :")
    pay_rate = float(input('Please enter your hourly pay rate. :')) # user inputs pay rate
    if pay_rate in range(7,500): # handle the bad
         print("Thank you")
    else:
        input("Please enter your pay rate between 7 and 500. :")
    return 'Name:',name,'Age:',age,'Rate:',pay_rate, # Prints the inputs as a string
from Assignments import weekly_pay
print(get_user_input())

if __name__ == 'main':
    get_user_input()  # function call


