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

rate = float(input('Please enter your hourly pay rate. :')) # user inputs pay rate
if rate in range(7,500): # handle the bad
    print("Thank you")
else:
    input("Please enter your pay rate between 7 and 500. :")
print('Name:',name,'\nAge:',age,'\nRate:',rate, sep="\n") # Prints the inputs as a string

if __name__ == '__main__':
    get_user_input()  # function call
