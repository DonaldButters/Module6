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



