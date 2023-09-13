#!/usr/bin/python3

import random


def get_joke(the_range, j_list, b_list):
    '''Take a range number, a list of text, and list of used indexes
    and prints out a string from the first list'''
    while True:
        selector = random.randrange(0,1000) % the_range  
        if selector not in b_list:
            break
        if len(b_list) == the_range:
            print(f"I'm all out of joke. Smell ya later...")
            exit(0)
    print(f"\n{j_list[selector]}\n")
    return selector


jokes = [
    "What's black, white, black, white, and green?",  # 0
    "What's red and smells like blue paint?",         # 1
    "What's green and has wheels?",                   # 2
    "What is a pirate's favorite letter?"             # 3
]

answers = [
    "Two skunks fighting over a pickle.",
    "Red paint.",
    "The grass. I lied about the wheels.",
    "You think it be 'R,' but it be the 'C.'"
]

item_count = len(jokes)
used = []
another = 'a'

while True:
    while True:
        user_input = input(f"Do you want to hear {another} joke? (y/n) ")
        if user_input == 'y':
            another = "another"
            break
        else:
            print(f"You're no fun :( Smell you later...")
            exit(1)
    index = get_joke(item_count, jokes, used)
    input(f"Hit enter when you give up.")
    print(f"\n{answers[index]}\n")
    used.append(index)
