#!/usr/bin/env python3

import os
import random
import operator


def get_operands(oper):
    '''Provides appropriate operands depending on the operator provided'''
    rand_tuple = {
        '+': (0, 100),
        '-': (2,100),
        '*': (0,12),
        '/': (1, 144)
    }
    if oper in ['+', '*']:
        a = random.randint(rand_tuple[oper])
        b = random.randint(rand_tuple[oper])
    elif oper == '-':
        # Loops if answer is going to be a negative number
        while True:
            a = random.randint(rand_tuple[oper])
            b = random.randint(rand_tuple[oper])
            if a >= b:
                break
    elif oper == '/':
        # Will loop until divisor goes into dividend evenly
        while True:
            a = random.randint(rand_tuple[oper])
            b = random.randint(rand_tuple[oper])
            if a % b == 0:
                break
    else:
        raise ValueError("Something went sideways with get_operands")
    
    return a, b


def do_math(op):
    '''Takes operator and does math with it'''

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    problem_number = 1
    correct = 0

    # User decides how many problems to solve
    while True:
        try:
            possible = int(input("How many problems to you want to do:"))
            if possible > 100:
                print(f"😳 {possible} is too many...")
            elif possible <= 0:
                print(f"😉 Uh...!? it's got to be more than 0")
            else:
                break
        except ValueError:
            print("That's not a number, silly")

    # Generates random problems with given operator
    while problem_number <= possible:
        # Finds random operands based on operation selected
        x, y = get_operands(op)
        right_answer = int(operators[op](x, y))

        # Gets answer, making sure it's an integer
        while True:
            try:
                user_answer = int(input(f"{x} {op} {y} = "))
                break
            except ValueError:
                print("That's not a number, silly")
        if user_answer == right_answer:
            print("Correct")
            correct += 1
        else:
            print(f"Incorrect. {x} {op} {y} = {right_answer}")

        problem_number += 1
    
    percentage = correct / possible * 100
    print(f"You got {percentage}% ({correct}/{possible})")


def get_option(options):
    '''Get's the option from the user'''
    while True:
        option = input(': ')
        if option in options:
            return option
        else:
            print(f"{option} is not in the list of options")


def main():
    '''The Main event'''
    options = {
        'a': '+',  # Addition
        's': '-',  # Subtraction
        'm': '*',  # Multiplication
        'd': '/',  # Division
        'e': 'exit',  # Exit
        'q': 'exit',  # Exit
        'x': 'exit'   # Exit
    }

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"===== Welcome to Math Game ======")

    while True:
        option = get_option(options)
        if option in ["q", "x", "e"]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n   Thanks for playing. Come again soon! 👋\n')
            break
        do_math(options[option])


main()