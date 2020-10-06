"""

Program: string_functions.py

Author: Donald Butters

Last date modified: 10/5/2020

The purpose of this program is to ask for a name and lucky number
whe the correct input is put in it will print out That is a lucky number
and then print the persons name the same number as their lucky number

:param parameter_1: User inputs a name
:param Parameter_2: User inputs a luck number
:returns Prints the persons name the number of the luck number
:raises keyError: asks for the input again


"""
def multiply_string():
    x = input('Enter your name: ')
    n = int(input('Enter your lucky number between 1-9:'))
    if n in range(1,11):
        print('That IS a luck number!')
    else:
        int(input('Enter a lucky number between 1-9 : '))
    return (x*n)

print(multiply_string())

