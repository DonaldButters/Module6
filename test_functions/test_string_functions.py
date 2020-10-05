def multiply_string():
    x = input('Enter your name: ')
    n = int(input('Enter your lucky number between 1-9:'))
    if n in range(1,11):
        print('That IS a lucky number!')
    else:
        int(input('Enter a lucky number between 1-9 : '))
    return (x*n)

print(multiply_string())

