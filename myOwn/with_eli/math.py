#!/usr/bin/env python3

import os
import random
import operator
try:
    from colorama import init as c_init
    from colorama import Fore, Style
except ModuleNotFoundError:
    print(
        '''Import Error: You don't have colorama installed.\n'''
        '''run: pip3 install colorama'''
    )


# Sometimes the world needs color
c_init()
global c_bl; c_bl = Fore.BLUE       # cyan 
global c_cy; c_cy = Fore.CYAN       # cyan 
global c_gr; c_gr = Fore.GREEN      # green 
global c_rd; c_rd = Fore.RED        # red 
global c_yl; c_yl = Fore.YELLOW     # yellow 
global c_dm; c_dm = Style.DIM       # dim 
global c_br; c_br = Style.BRIGHT    # bright 
global c_r;  c_r = Style.RESET_ALL  # reset color - needed to terminate color


def specify_multiplier():
    # Can sepecify all a specific multiplier
    while True:
        mul_opt = input(f"Specify a multiplier (2 - 12) or 'm' for mixed: ")
        try:
            # If it's an integer in range
            mul_opt = int(mul_opt)
            if mul_opt in list(range(2, 13)):
                break
        except ValueError:
            # Or if it's m for mixed
            if mul_opt == 'm':
                break
            else:
                continue
    return mul_opt    


def get_operands(m_spec, oper):
    '''Provides appropriate operands depending on the operator provided'''
    rand_tuple = {
        '+': (10, 100),
        '-': (1, 100),
        '×': (2, 12),
        '÷': (2, 144)
    }
    if oper == '+':
        a = random.randint(*rand_tuple[oper])
        b = random.randint(*rand_tuple[oper])
    elif oper == '×':
        if m_spec == 'm':
            a = random.randint(*rand_tuple[oper])
            b = random.randint(*rand_tuple[oper])
        else:
            while True:
                # only break when one of the multipliers is the specified integer
                a = random.randint(*rand_tuple[oper])
                b = random.randint(*rand_tuple[oper])
                if a == m_spec or b == m_spec:
                    break
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
        raise ValueError(f"{c_rd}Something went sideways with get_operands{c_r}")
    
    return a, b


def do_math(op):
    '''Takes operator and does math with it'''

    max_probs = 132
    multiple_specification = None

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '×': operator.mul,
        '÷': operator.truediv
    }

    problem_number = 1
    correct = 0
    silly = f"🙈 {c_yl}That's not a number, silly{c_r} 😖"

    # User decides how many problems to solve
    while True:
        try:
            possible = int(input(f"How many problems to you want to do (between 1 and {max_probs}): "))
            if possible > max_probs:
                print(f"😳 {c_yl}{possible} is too many...{c_r}")
            elif possible <= 0:
                print(f"😉 {c_br}{c_bl}Uh...!? it's got to be more than 0{c_r}")
            else:
                break
        except ValueError:
            print(silly)

    # If multiplying, then you can choose to specify a multiplier
    if op == '×':
        multiple_specification = specify_multiplier()

    # Generates random problems with given operator
    while problem_number <= possible:
        # Finds random operands based on operation selected
        x, y = get_operands(multiple_specification, op)
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
    print("===== Welcome to Math Game ======")
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