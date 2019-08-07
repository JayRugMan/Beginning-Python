#!/usr/bin/python3
# playing around with string methods

import time


def theLongAndShort(mystring):
    # Expands string by lengthening the space the string is joined by
    for spaces in range(12):
        print('{}'.format(' ' * spaces).join(list(mystring)))
        time.sleep(0.5)
    # Makes the "point" of the "arrowhead" by expanding by 12 spaces
    print('{}'.format(' ' * 12).join(list(mystring)))
    time.sleep(0.5)
    # contracts string by shortening the space the string is joined by
    for spaces in range(11, -1, -1):
        print('{}'.format(' ' * spaces).join(list(mystring)))
        time.sleep(0.5)


def main():
    userInput = input('Enter a string to stretch (at least two characters): ')
    theLongAndShort(userInput)


main()
