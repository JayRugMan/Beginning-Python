#!/usr/bin/python
""" Version 1.1 - Structure
- Put everything into functions
- created a main function
- added comments to each function
- appended each functions input arguments with argument type
- added needed white space
- reduced line size
    Version 1.2 - Consolidation
- combine functions turning_right and turning_left
- instead of clearing screen in main funtion just
    before calling main_display, it is now cleared
    in main_display
- added upser input to the main_display function
- created a function to initialize the main arguments
- moved function comments from outside the function to within
- randomized the initial direction and room
- made forward a function to clean up main
- modified the turn function to include feedback
"""

import os
import random


# Generates and returnes a random password
def random_password():  ##JH UPDATED and USED
    """takes no arguments
    returns a random password from a list of passwords
    depends on imported random"""

    password_list = ['sandman', 'Lockhead', 'Babling brooK', 'Santa Claus',
                     'Peanut', 'fury flurry', 'clinician', 'random PassWord']

    p_word_picker = random.randint(0, (len(password_list) - 1))
    pw = password_list[p_word_picker]

    return pw


# Takes user input and compares it to argument entered
def password_challenge(pw):
    # takes "password"
    # returns true or false
    # depends on imported os

    os.system('cls' if os.name == 'nt' else 'clear')

    user_guess = input('\nWhat is the password? ')

    if user_guess == pw:
        return True

    else:
        return False


def build_house(password):  ##JH UPDATED and USED
    """Creates the house dictionary, as well as rooms and directions list"""

    house = {
        'foyer': {
            'north': 'a locked door',
            'east': 'a map',
            'south': 'the exit',
            'west': 'an open door'},
        'parlor': {
            'north': 'an open door',
            'east': 'an open door',
            'south': 'a wall',
            'west': 'a wall'},
        'study': {
            'north': 'an open door',
            'east': password,
            'south': 'a wall',
            'west': 'a wall'},
        'master bedroom': {
            'north': 'a wall',
            'east': 'an open door',
            'south': 'an open door',
            'west': 'a wall'},
        'kitchen': {
            'north': 'a map',
            'east': 'a wall',
            'south': 'an open door',
            'west': 'an open door'},
        'bathroom': {
            'north': 'a wall',
            'east': 'a wall',
            'south': 'an open door',
            'west': 'a wall'},
        'feedback': 'Welcome to my old house.',  # updated as needed throught
    }
    rooms = ['foyer', 'parlor', 'study',
             'master bedroom', 'kitchen', 'bathroom']
    directions = ['north', 'east', 'south', 'west']

    return house, rooms, directions


def define_player(rooms, directions):  ##JH UPDATED and USED
    """Sets initial room and direction randomly"""

    room = rooms[random.randint(0, 4)]  # does not include locked room
    direction = directions[random.randint(0, 3)]
    player = {
        'room': room,
        'direction': direction,
        'won': False
    }

    return player


def hud(house, room, direction):  ##JH UPDATED and USED
    """Prints HUD with which room your in, which direction you're facing, What's
    straight ahead, and what the feedback is from the host of the house"""

    os.system('cls' if os.name == 'nt' else 'clear')
    ahead = house[room][direction]
    feedback = house['feedback']

    print("""=== This Old House ===

You are in the {} facing {}

straight ahead is {}

== Options ==
l = turn left
r = turn right
f = move forward
q = quit

"{}"
"What would you like to do?"
""".format(room, direction, ahead, feedback))

    return


def turn(data, directions, direction, r_or_l):  ##JH UPDATED and USED
    """Changes direction base on user input"""

    last_index = len(directions) - 1
    dir_index = directions.index(direction)

    if r_or_l == 'l':
        if dir_index == 0:
            direction = directions[last_index]
        else:
            direction = directions[dir_index-1]

    elif r_or_l == 'r':
        if dir_index < last_index:
            direction = directions[dir_index+1]
        else:
            direction = directions[0]

    data['feedback'] = 'take a look around'
    return direction


##JH def clean_input(input_type):
##JH     """ Cleans input based on what i """


# Clears the screen and displays map until enter is pressed
def display_map():
    # no arguments taken or returned
    # depends on imported os

    os.system('cls' if os.name == 'nt' else 'clear')

    print("""                 === MAP of my house ===

                         -NORTH-

  +----------------+--------M-------+-----------------+
| |                |                |                 | |
W | master bedroom D     kitchen    |    bathroom     | E
E |                |                |                 | A
S +--------D-------+--------D-------+--------D--------+ S
T |                |                |                 | T
| |     study      |     parlor     D      foyer      M |
  |                |                |                 |
  +----------------+----------------+--------E--------+

                        -SOUTH-
""")

    input("\t      hit ENTER once you're done")
    return


def forward(house, rooms, room, direction):
    """Resonds to the users selection to move forward"""

    ahead = house[room][direction]

    if ahead == 'an open door':
        room = change_rooms(int_in_which_room, int_facing_which_direction)
        # if you make it into room 5 (bathroom),
        # you win and can only go into room 1 and exit
        # your direction also changes to south
        if int_in_which_room == 5:
            house['feedback'] = 'You get the treasure, now leave in peace.'
            bul_won = True
            int_facing_which_direction = 2
            str_house_0_west = 'a closed door'
        # if not in room five, feedback is
        # given that you are in a new room
        else:
            str_feedback = "You're in a new room"

    # if the door is locked and you move forward,
    # you are challenged for a password
    elif ahead == 'a locked door':
        # if you get the password right, the
        # locked door becomes an open door
        if password_challenge(str_password):
            str_feedback = 'You guessed right'
            str_house_0_north = 'an open door'
        # otherwise, the door stays
        # locked and the password changes
        else:
            str_feedback = 'You guessed wrong. It is written anew.'
            str_password = random_password()
            str_house_2_east = str_password

    # if you see a wall, you're scolded, but given hope
    elif ahead == 'a wall':
        str_feedback = "You can't walk through walls yet"

    # if you see an exit, you leave the game by going forward
    elif ahead == 'the exit':
        str_user_input = 'q'

    # the door to the parlor - or rest of the
    # house - closed once you enter the bathroom
    elif ahead == 'a closed door':
        str_feedback = 'You have your treasure, please leave.'

    # if you see a map, you get to find where you are
    elif ahead == 'a map':
        display_map()
        str_feedback = "don't get lost now"

    return (int_in_which_room, str_feedback, bul_won,
            int_facing_which_direction, str_house_0_west, str_house_0_north,
            str_password, str_house_2_east, str_user_input)


# moves you to a new room
def change_rooms(int_old_room, int_facing_which_direction):
    # takes interger argument for old room and direction
    # returns new room
    # This is manually configured based on the structure and
    # layout of the house defined in build_house()

    # if you were in the foyer
    if int_old_room == 0:
        if int_facing_which_direction == 0:  # and if you are facing north
            new_room = 5  # you will enter the bathroom
        elif int_facing_which_direction == 3:  # and if you are facing west
            new_room = 1  # you will enter the parlor

    # if you are in the parlor
    elif int_old_room == 1:
        if int_facing_which_direction == 1:  # and if you are facing east
            new_room = 0  # you will enter the foyer
        elif int_facing_which_direction == 0:  # and if you are facing north
            new_room = 4  # you will enter the kitchen

    # if you are in the study
    elif int_old_room == 2:
        new_room = 3  # you will enter the master bedroom

    # if you are in the master bedroom
    elif int_old_room == 3:
        if int_facing_which_direction == 1:  # and if you are facing east
            new_room = 4  # you will enter the kitchen
        elif int_facing_which_direction == 2:  # and if you are facing south
            new_room = 2  # you will enter the study

    # if you are in the kitchen
    elif int_old_room == 4:
        if int_facing_which_direction == 2:  # and if you are facing south
            new_room = 1  # you will enter the parlor
        elif int_facing_which_direction == 3:  # and if you are facing west
            new_room = 3  # you will enter the master bedroom

    # if you are in the bathroom
    elif int_old_room == 5:
        new_room = 0  # you will enter the foyer

    return new_room


# Main function
def main_old():

    # call function to initialize the following arguments
    (directions, facing_which_direction, in_which_room, house, room_names,
     password, what_you_see, feedback, user_input, won) = initialize_args()

    while(user_input != 'q'):

        user_input = main_display(room_names, in_which_room,
                                  directions, facing_which_direction,
                                  what_you_see, feedback)

        if user_input == 'l' or user_input == 'r':
            # the fucntion to turn is called
            trng = turning(user_input, facing_which_direction, directions)
            facing_which_direction, feedback = trng

        elif user_input == 'f':
            (in_which_room, feedback, won, facing_which_direction,
             house[0]['west'], house[0]['north'], password, house[2]['east'],
             user_input
             ) = forward(what_you_see, in_which_room, feedback, won,
                         facing_which_direction, house[0]['west'],
                         house[0]['north'], password,
                         house[2]['east'], user_input)

        what_you_see = house[in_which_room][directions[facing_which_direction]]

    os.system('cls' if os.name == 'nt' else 'clear')

    if won:
        print("\n\tCongradulations!!\n\tSpend it on charity, will ya?!\n")

    else:
        print('\n\tSmell you later!\n')


def main():
    'Main Function'

    # Set random password
    password = random_password()
    # Build House and include password on one of the walls
    house, rooms, directions = build_house(password)
    # Initialize player with start room, direction, and "won" status
    player = define_player(rooms, directions)
    # Enter gameplay loop
    while True:
        # Heads Up Display
        hud(house, room, direction)
        # Get User input
        user_input = input(': ').lower()
        if user_input == 'q':  # quit if q
            break
        elif user_input == 'l' or user_input == 'r':  # turn in l or r
            direction = turn(house, directions, direction, user_input)
        elif user_input == 'f':  # move forward or interact with what's ahead
            room = forward(house, rooms, room, direction)

    os.system('cls' if os.name == 'nt' else 'clear')
    if player['won']:
        print("\n\tCongradulations!!\n\tSpend it on charity, will ya?!\n")
    else:
        print('\n\tSmell you later!\n')


main()
