#!/usr/local/bin/python3.7
# playing around with string methods

import time


def theLongAndShort(mystring):
    for spaces in range(12):
        print('{}'.format(' ' * spaces).join(list(mystring)))
        time.sleep(0.5)
    for spaces in range(11, -1, -1):
        print('{}'.format(' ' * spaces).join(list(mystring)))
        time.sleep(0.5)


def main():
    userInput = input('Enter a string to stretch: ')
    theLongAndShort(userInput)


main()
