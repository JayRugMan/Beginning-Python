#!/usr/bin/env python3

import os
import random
import operator


def get_operands(oper):
    '''Provides appropriate operands depending on the operator provided'''
    rand_tuple = {
        '+': (10, 100),
        '-': (1, 100),
        '×': (2, 12),
        '÷': (2, 144)
    }
    if oper in ['+', '×']:
        a = random.randint(*rand_tuple[oper])
        b = random.randint(*rand_tuple[oper])
    elif oper == '-':
        # Loops if answer is going to be a negative number
        while True:
            a = random.randint(*rand_tuple[oper])
            b = random.randint(*rand_tuple[oper])
            if a > b:
                break
    elif oper == '÷':
        # Will loop until divisor goes into dividend evenly
        while True:
            a = random.randint(*rand_tuple[oper])
            b = random.randint(*rand_tuple[oper])
            if a % b == 0 and a != b and (a/b) <= 12 and b <= 12:
                break
    else:
        raise ValueError("Something went sideways with get_operands")
    
    return a, b


def do_math(op):
    '''Takes operator and does math with it'''

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '×': operator.mul,
        '÷': operator.truediv
    }

    problem_number = 1
    correct = 0
    silly = "  🙈 That's not a number, silly 😖"

    # User decides how many problems to solve
    while True:
        try:
            possible = int(input("How many problems to you want to do (between 1 and 100): "))
            if possible > 100:
                print(f"😳 {possible} is too many...")
            elif possible <= 0:
                print(f"😉 Uh...!? it's got to be more than 0")
            else:
                break
        except ValueError:
            print(silly)

    # Generates random problems with given operator
    while problem_number <= possible:
        # Finds random operands based on operation selected
        x, y = get_operands(op)
        right_answer = int(operators[op](x, y))

        # Gets answer, making sure it's an integer
        while True:
            try:
                user_answer = int(input(f"\n{problem_number:3}: {x} {op} {y} = "))
                break
            except ValueError:
                print(silly)
        if user_answer == right_answer:
            print("  🏅 Correct! 🏅")
            correct += 1
        else:
            print(f"  💩 Incorrect. {x} {op} {y} = {right_answer}")

        problem_number += 1
    
    percentage = correct / possible * 100
    print(f"\n\nYou got {percentage}% ({correct}/{possible})")
    input("\nHit ENTER to clear screen for menu...")


def get_option(options):
    '''Get's the option from the user'''
    while True:
        option = input('\n: ')
        if option in options:
            return option
        else:
            print(f"🙈 {option} is not in the list of options 😖")


def print_menu():
    '''Takes list of options to print a menu'''
    opts = {
        'a': "Addition (+)",
        's': "Subtraction (-)",
        'm': "Multiplication (×)",
        'd': "Division (÷)",
        'e/q/x': "Exit"
    }
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"===== Welcome to Math Game ======")
    print("\n-- Choose an operation --\n")
    for key,value in opts.items():
        print(f" {key:5} - {value}")



def main():
    '''The Main event'''
    options = {
        'a': '+',  # Addition
        's': '-',  # Subtraction
        'm': '×',  # Multiplication
        'd': '÷',  # Division
        'e': 'exit',  # Exit
        'q': 'exit',  # Exit
        'x': 'exit'   # Exit
    }

    while True:
        print_menu()
        option = get_option(options)
        if option in ["q", "x", "e"]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n   Thanks for playing. Come again soon! 👋\n')
            break
        do_math(options[option])


main()