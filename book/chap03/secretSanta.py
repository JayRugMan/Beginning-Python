#!/usr/local/bin/python3.7
# This program should help in drawing names for secret santa

import os
from random import shuffle

# Get names into names list
names = []
entry = ''
while entry != 'done':
    entry = input('Enter name (or "done" when done): ')
    if entry != 'done':
        names.append(entry)

# Make a shuffled copy of list
shuffled_names = names[:]
shuffle(shuffled_names)  # Not really shuffled until this

# Match names in lists to make assignments
count = len(names)
assignments = []
for i in range(count):
    assignments.append('{} has {}'.format(names[i], shuffled_names[i]))

# Print names, one at a time, clearing the screen each time
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    # prints unmbered list of names
    count = 1

    for name in names:
        print('{} - {}'.format(count, name))
        count += 1

    entry = input('Enter your number to see your assignment ("0" if done): ')
    entry = int(entry)
    if entry == 0:  # Exits loop if '0' is entered
        break

    name_index = entry - 1
    output = '\n{}. Write it down (if you have you, buy you something nice;) )'
    print(output.format(assignments[name_index]))
    input('\nType enter to continue clear screen for next person.')
