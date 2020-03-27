#!/usr/bin/python3


def calculator():
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(int(x/y))


try:
    calculator()
except (ZeroDivisionError, ValueError, TypeError, NameError) as e:
    print(e)
