#!/usr/bin/python3
'''This program will take a number, then run it through the 3x+1 algorithm,
returning the elevation of the number, or the highest interger reached while
processing provided number through the algorithm, as well as the number of
iterations taken to get to 1(assuming all integers eventually get to 1 ;) )
 - Some interesting numbers to try are 27 and 9663
'''

import sys


def number_is_good(the_num):
    '''test if argument is an integer, greater than 0'''
    try:
        the_num = int(the_num)
        if the_num < 0:
            print("That's negative!")
            return False
        if the_num == 0:
            print("That's not a non-zero integer!")
            return False
        return True
    except ValueError:
        print("That's not an integer!")
        return False


def get_number():
    '''gets a positive, non-zero integer'''
    print('Enter any positive, non-zero integer')
    while True:
        the_number = input(': ')
        if number_is_good(the_number):
            break
    return int(the_number)


def algorithm(the_int):
    '''Runs integer through interated algorithm: if integer is even, it's,
    halved, if it's odd, it's multiplied by three and added to 1, all the
    way down to 1. The number of times it loops (total stopping time), as
    well as the highest number it reaches are returned'''
    elvtn = the_int
    count = 0
    while True:
        if the_int == 4:  # prevent eternal 4 > 2 > 1 > 4 ... loop
            count += 2  #  4/2=2 > 2/1=1, so 2 more on the count
            break
        if the_int % 2:  # if the_int is odd, or modulous is 1 (also "True")
            the_int = (the_int * 3) + 1
            count += 1
            if the_int > elvtn:
                elvtn = the_int
            continue
        the_int = int(the_int/2)
        count += 1
    return elvtn, count


def print_output(num, elev, i):
    '''prints formatted output'''
    output_str = '{0:<26} {1}'
    lines_dict = {
        'Chosen Integer:': num,
        'Highest number reached:': elev,
        'Total Stop Time:': i
    }
    for key, val in lines_dict.items():
        print(output_str.format(key, val))


def main(arg='nothing'):
    '''Main event'''
    if arg == 'nothing':
        integer = get_number()
    else:
        integer = arg
    elevation, iteration = algorithm(integer)
    print_output(integer, elevation, iteration)


try:
    user_arg = sys.argv[1]
    if number_is_good(user_arg):
        main(int(user_arg))
except IndexError:
    main()
