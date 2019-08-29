#!/usr/bin/python3
# This program should help in drawing names for secret santa

import os
from random import shuffle


def getNames():
    # Get names into names list
    nms = []
    prompt = 'Enter name (or "done" when done): '

    while True:
        entry = input(prompt)
        if entry != 'done' and entry != '':
            nms.append(entry)
        if entry == 'done':
            break

    return nms


def areMatches(lst1, lst2):
    # This function makes sure nobody gets assigned themselves
    # by returning 'True' if any index in first list matches
    # same index in second list, or 'False' if there are no
    # matches
    for itm1, itm2 in zip(lst1, lst2):
        if itm1 == itm2:
            return True

    return False


def shuffleNames(nms):
    # Copies list of names and shuffles the copy
    shuf_nms = nms[:]

    # loops until all no indexes match between lists
    while areMatches(nms, shuf_nms):
        shuffle(shuf_nms)  # Not really shuffled until this

    return shuf_nms


def makeAssignments(nms, shuf_nms):
    # Matches names in lists to make assignments
    filter = ['and', '&', '+']
    assgnmnts = []
    for nm, assgnmnt in zip(nms, shuf_nms):
        # if the name is really two people (contains any form of "and"), the
        # "to be" verb is conjegated accordingly - For good grammer :)
        if any([True for f in filter if f in nm]):
            toBe = 'have'
        else:
            toBe = 'has'
        assgnmnts.append('{} {} {}'.format(nm, toBe, assgnmnt))

    return assgnmnts


def userSelect(nms):
    # gets users number associated with name from list
    prompt = '\nEnter your number to see your assignment ("0" to exit): '
    rng = range(len(nms) + 1)

    # loops while entry is not integer or in range
    while True:
        try:
            entry = int(input(prompt))
            if entry in rng:
                break
            else:
                print("\tWoa cowboy, that number's out of range")
        except ValueError:
            print("\tHey, that's not a number")

    return entry


def giveResults(nms, assgnmnts):
    # Print assignments, one at a time, clearing the screen each time
    while True:
        # Clears the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Prints numbered list of names
        print()
        for lst_num, nm in enumerate(nms, 1):
            print('\t{} - {}'.format(lst_num, nm))

        # Asks for selection, verifies it's a number in range of options
        selection = userSelect(nms)
        # Exits if 0 is selected
        if selection == 0:
            break

        # If selection is accepted and not zero,
        # the name's assignment is printed
        nm_ndx = selection - 1
        output = '\n{}. Write it down!'
        print(output.format(assgnmnts[nm_ndx]))
        input('\nHit enter to clear screen and continue with next person.')


def main():
    names = getNames()
    shuffled_names = shuffleNames(names)
    assignments = makeAssignments(names, shuffled_names)
    giveResults(names, assignments)


main()
