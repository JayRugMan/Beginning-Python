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
    # by returning 'True' if any index in first list matched
    # same index in second list, or 'False' if there are no
    # matches
    rng = len(lst1)
    for i in range(rng):
        if lst1[i] == lst2[i]:
                return True

    return False


def shuffleNames(nms):
    # Make a shuffled copy of list
    shuf_nms = nms[:]
    while areMatches(nms, shuf_nms):
        shuffle(shuf_nms)  # Not really shuffled until this

    return shuf_nms


def makeAssignments(nms, shuf_nms):
    # Match names in lists to make assignments
    rng = len(nms)
    assgnmnts = []
    for i in range(rng):
        assgnmnts.append('{} has {}'.format(nms[i], shuf_nms[i]))

    return assgnmnts


def listNames(nms):
    # prints unmbered list of names
    count = 1
    for name in nms:
        print('{} - {}'.format(count, name))
        count += 1


def userSelect(nms):
    # gets users number associated with name from list

    prompt = 'Enter your number to see your assignment ("0" to exit): '
    rng = range(len(nms) + 1)
    int_in_rng = False  # for checking whether is an integer in range

    # loops while entry is not integer or in range
    while not int_in_rng:
        entry = input(prompt)
        try:
            entry = int(entry)
            if entry in rng:
                int_in_rng = True
            else:
                print("That number's out of range")
        except ValueError:
            print("That's not a number")

    # Clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    return entry


def seeAssignment(nms, assgnmnts):
    # Gets uses selection and prints out secret Santa assignments

    # User selection - exits if '0' is selected
    slctn = userSelect(nms)
    if slctn == 0:
        return slctn

    # prints assignment
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
        # Clears the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # prints names list with numbers
        listNames(names)

        # Takes user input and prints corresponding secret Santa assignment
        selection = seeAssignment(names, assignments)
        if selection == 0:  # Exits loop if '0' is entered
            break


main()
