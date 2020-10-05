"""

Program: get_user_input.py

Author: Donald Butters

Last date modified: 10/5/2020

The purpose of this program is prompt a name, age, and hourly pay.
It then imports a function from weekly_pay.py and runs that function
Then the program out prints the new input

"""



def get_user_input(): # keyword def with function name then ():
     return 'Name:',name,'Age:',age,'Rate:',pay_rate,
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
    input('Please re-enter a valid number :')
from Assignments import weekly_pay # imports weekly_pay and runs it

