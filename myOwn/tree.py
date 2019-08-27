#!/usr/bin/python3
# Creates a tree of hash symbols based on the "height" entered by the user


def get_input():
    # Gets number of rows from user and puts into argument height
    prompt = {'ht': ' How tall should the tree be: ',
              'ndls': ' Pick a character for the needles: ',
              'tnk': ' Pick a character for the stump: '}
    print()
    # make sure entry is an integer
    while True:
        try:
            height = int(input(prompt['ht']))
            break
        except ValueError:
            continue
    # looking for one character
    while True:
        needles = input(prompt['ndls'])
        if len(needles) == 1: break
    # looking for one character
    while True:
        trunk = input(prompt['tnk'])
        if len(trunk) == 1: break
    print()
    return (height, needles, trunk)


def print_tree(level, needles):
    # Loops through each row of the tree, printing out the
    # number of hashes and left-whitespace based on "height"
    string = ' {0:<{buff}}{1:{1}^{tree}}'
    blank = ' '
    tree = 1
    while level > 0:
        print(string.format(blank, needles, buff=level, tree=tree))
        level -= 1
        tree += 2


def print_stump(level, trunk):
    # prints stump
    # Create a stump factor to determine the size of the stump
    # based on height - no less than 1
    string = ' {0:^{buff}}'
    stump_factor = int((level / 7)) or 1
    trunk = trunk * stump_factor
    # the stump gains a level for each 7 levels of the tree
    for row in range(stump_factor):
        print(string.format(trunk, buff=(level*2+1)))
    # Print a blank line at the end
    print()


def main():
    (height, needles, trunk) = get_input()
    print_tree(height, needles)
    print_stump(height, trunk)


main()
