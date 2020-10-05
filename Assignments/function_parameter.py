"""

Program: multiply_string.py

Author: Donald Butters

Last date modified: 10/5/2020

The purpose of this program is to ask for a number between 2-7
when the correct input is put in it will print out What is your
favorite class? and then print "Python! the correct number of times

"""
def multiply_string():
    x = 'Python'
    n = int(input('Enter a number between 2-7:'))
    if n in range(2,8):
        print('What is your favorite class?!')
    else:
        int(input('Enter a number between 2-7 : '))
    return (x*n)

print(multiply_string())


