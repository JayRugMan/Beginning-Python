#!/usr/bin/python3
# This program should help in drawing names for secret santa

import os
from random import shuffle


def getNames():
    # Get names into names list
    nms = []
    entry = ''
    prompt = 'Enter name (or "done" when done): '
    while entry != 'done':
        entry = input(prompt)
        if entry != 'done' and entry != '':
            nms.append(entry)

    return nms


def areMatches(lst1, lst2):
    # This function makes sure nobody gets assigned themselves
    isSame = False
    rng = len(lst1)
    for cnt in range(rng):
        if lst1[cnt] == lst2[cnt]:
                isSame = True

    return isSame


def shuffleNames(nms):
    # Make a shuffled copy of list
    shuffled_nms = nms[:]
    while areMatches(nms, shuffled_nms):
        shuffle(shuffled_nms)  # Not really shuffled until this

    return shuffled_nms


def makeAssignments(nms, shuffled_nms):
    # Match names in lists to make assignments
    rng = len(nms)
    assgnmnts = []
    for cnt in range(rng):
        assgnmnts.append('{} has {}'.format(nms[cnt], shuffled_nms[cnt]))

    return assgnmnts


def listNames(nms):
    # prints unmbered list of names
    count = 1
    for name in nms:
        print('{} - {}'.format(count, name))
        count += 1


def userSelect(nms):
    # gets users number associated with name from list
    prompt = 'Enter your number to see your assignment ("0" if done): '
    rng = range(len(nms) + 1)
    is_int_in_rng = False  # for checking whether is an integer

    # loops while entry is not integer or in range
    while not is_int_in_rng:
        entry = input(prompt)
        try:
            entry = int(entry)
            if entry in rng:
                is_int_in_rng = True
            else:
                print("That number's out of range")
        except ValueError:
            print("That's not a number")

    os.system('cls' if os.name == 'nt' else 'clear')

    return entry


def seeAssignment(nms, assgnmnts):
    # Gets uses selection and prints out secreSanta assignments
    slctn = userSelect(nms)
    if slctn == 0:
        return slctn

    # prints out assignment
    nm_ndx = slctn - 1
    output = '\n{}. Write it down!'
    print(output.format(assgnmnts[nm_ndx]))
    input('\nHit enter to clear screen and continue with next person.')


def main():
    names = getNames()
    shuffled_names = shuffleNames(names)
    assignments = makeAssignments(names, shuffled_names)
    selection = 1

    # Print assignments, one at a time, clearing the screen each time
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        listNames(names)

        selection = seeAssignment(names, assignments)
        if selection == 0:  # Exits loop if '0' is entered
            break


main()
