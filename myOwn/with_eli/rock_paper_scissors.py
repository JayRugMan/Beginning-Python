#!/usr/bin/python3

'''
Rock Paper Scissors
-------------------------------------------------------------
Modified code from:
https://hackr.io/blog/python-projects
'''


import random
import os
import re


def cs():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_rps():
    play = True
    cs()
    while play:
        user_choice = input('\nChoose your weapon'
                            ' [R]ock](1), [P]aper(2), or [S]cissors(3)'
                            ' (q or 4 to quit): ')

        if re.match("[Qq4]", user_choice):
            # Quits
            play = False
            continue
        elif not re.match("[SsRrPp123]", user_choice):
            cs()
            print(f"\nI don't know what weapon that is, man!")
            continue
        
        cs()

        choice_dict = {
            'r': 'Rock',
            'p': 'Paper',
            's': 'Scissors',
            '1': 'Rock',
            '2': 'Paper',
            '3': 'Scissors',
        }
        user_weapon = choice_dict[user_choice.lower()]

        print('\nRock, Paper, Scissors - Shoot!')
        print(f'\nYou chose: {user_weapon}')

        choices = ['r', 'p', 's']
        opp_choice = random.choice(choices)
        opp_weapon = choice_dict[opp_choice]

        print(f'I chose: {opp_weapon}')

        if opp_weapon == user_weapon:
            print('Tie!')
        elif opp_weapon == 'Rock' and user_weapon == 'Scissors':
            print(f'{opp_weapon} beats {user_weapon.lower()}, I win!')
        elif opp_weapon == 'Scissors' and user_weapon == 'Paper':
            print(f'{opp_weapon} beats {user_weapon.lower()}, I win!')
        elif opp_weapon == 'Paper' and user_weapon == 'Rock':
            print(f'{opp_weapon} beats {user_weapon.lower()}, I win!')
        else:
            print(f'{user_weapon} beats {opp_weapon.lower()}, you win!')
    cs()
    print('Thanks for playing!')


if __name__ == '__main__':
   play_rps()