"""

Program: validate_input_in_functions.py

Author: Donald Butters

Last date modified: 10/5/2020

The purpose of this program is to ask for the name of a test
then ask for a test score
then prints the test name and score

:param parameter_1: User inputs a Test Name
:param Parameter_2: User inputs a Test Score
:returns Prints Test Name the Test Score
:raises keyError: invalid message


"""
def score_input():
    test_name = input('Enter Test Name :')
    test_score = int(input('Enter your Test Score :'))
    invaild_message = 'Invalid test score, try again!'
    if test_score in range(1,100):
        print('thank you')
    else:
        print(invaild_message)
    return ('Test name:',test_name,'Test Score:',test_score)
print(score_input())



