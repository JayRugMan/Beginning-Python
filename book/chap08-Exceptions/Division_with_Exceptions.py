#!/usr/bin/python3


def calculator():
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(int(x/y))


try:
    calculator()
except ZeroDivisionError:
    print("The second number can't be zero.")
except ValueError:
    print("That entry isn't a number.")
