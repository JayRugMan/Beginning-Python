#!/usr/bin/python3
# This program should help in drawing names for secret santa

import os
from random import shuffle


def areMatches(lst1, lst2):
    # This function makes sure nobody gets assigned themselves
    isSame = False
    rng = len(lst1)
    for cnt in range(rng):
        if lst1[cnt] == lst2[cnt]:
            isSame = True
    return isSame


# Get names into names list
names = []
entry = ''
while entry != 'done':
    entry = input('Enter name (or "done" when done): ')
    if entry != 'done':
        names.append(entry)

# Make a shuffled copy of list
shuffled_names = names[:]
while areMatches(names, shuffled_names):
    shuffle(shuffled_names)  # Not really shuffled until this

# Match names in lists to make assignments
count = len(names)
assignments = []
for i in range(count):
    assignments.append('{} has {}'.format(names[i], shuffled_names[i]))

# Print assignments, one at a time, clearing the screen each time
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    # prints unmbered list of names
    count = 1
    for name in names:
        print('{} - {}'.format(count, name))
        count += 1

    # gets users number associated with name from list
    entry = input('Enter your number to see your assignment ("0" if done): ')
    entry = int(entry)
    os.system('cls' if os.name == 'nt' else 'clear')
    if entry == 0:  # Exits loop if '0' is entered
        break

    # prints out assignment
    name_index = entry - 1
    output = '\n{}. Write it down!'
    print(output.format(assignments[name_index]))
    input('\nHit enter to clear screen and continue with next person.')
