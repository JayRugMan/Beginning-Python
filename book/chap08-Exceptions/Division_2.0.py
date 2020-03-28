#!/usr/bin/python3
while True:
    try:
        x = int(input('Enter the first number (x): '))
        y = int(input('Enter the second number (y): '))
        value = x/y
        print('x/y is {}'.format(value))
    except:
        print('Invalid input. Please try again.')
    else:
        break
