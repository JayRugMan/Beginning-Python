#!/usr/bin/python3
# Creates a tree of hash symbols based on the "height" entered by the user


def get_input():
    # Gets number of rows from user and puts into argument height
    tree_char = 'vv'
    stump_char = '##'
    check = True
    print()
    while check:  # make sure entry is an integer
        height = input(' How tall should the tree be: ')
        try:
            height = int(height)
            check = False
        except ValueError:
            check = True
    while len(tree_char) != 1:  # looking for one character
        tree_char = input(' Pick a character for the tree: ')
    while len(stump_char) != 1:  # looking for one character
        stump_char = input(' Pick a character for the stump: ')
    print()
    return (height, tree_char, stump_char)


def print_tree(height, needles):
    # Loops through each row of the tree, printing out the
    # number of hashes and left-whitespace based on "height"
    blank = ' '
    tree = 1
    while height > 0:
        print(' {0:<{buff}}{1:{1}^{tree}}'.format(blank,
                                                  needles,
                                                  buff=height,
                                                  tree=tree))
        height -= 1
        tree += 2


def print_stump(height, wood):
    # prints stump
    # Create a stump factor to determine the size of the stump
    # based on height - no less than 1
    stump_factor = int((height / 7)) or 1
    wood = wood * stump_factor
    # the stump gains a level for each 7 levels of the tree
    for row in range(stump_factor):
        print(' {0:^{buff}}'.format(wood, buff=(height*2+1)))
    # Print a blank line at the end
    print()


def main():
    (height, needles, wood) = get_input()
    print_tree(height, needles)
    print_stump(height, wood)


main()
