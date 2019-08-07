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


def getNames():
    # Get names into names list
    nms = []
    entry = ''
    prompt = 'Enter name (or "done" when done): '
    while entry != 'done':
        entry = input(prompt)
        if entry != 'done':
            nms.append(entry)
    return nms


def shuffleNames(nms):
    # Make a shuffled copy of list
    shuffled_nms = nms[:]
    while areMatches(nms, shuffled_nms):
        shuffle(shuffled_nms)  # Not really shuffled until this
    return shuffled_nms


def makeAssignments(nms, shuffled_nms):
    # Match names in lists to make assignments
    count = len(nms)
    assignments = []
    for i in range(count):
        assignments.append('{} has {}'.format(nms[i], shuffled_nms[i]))
    return assignments
##JH  Pick up here ##

def main
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
