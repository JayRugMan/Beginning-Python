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


def random_password():  ##JH UPDATED and USED
    """Returns a random password from a list of passwords
    depends on imported random"""

    password_list = ['sandman', 'Lockhead', 'Babling brooK', 'Santa Claus',
                     'Peanut', 'fury flurry', 'clinician', 'random PassWord']

    p_word_picker = random.randint(0, (len(password_list) - 1))
    pw = password_list[p_word_picker]

    return pw


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
        'feedback': 'Welcome to my old house.',  # updated as needed throughout
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
        'facing': direction,
        'won': False
    }

    return player


def hud(house, player):  ##JH UPDATED and USED
    """Prints HUD with which room your in, which direction you're facing, What
    is straight ahead, and what the feedback is from the host of the house"""

    os.system('cls' if os.name == 'nt' else 'clear')
    ahead = house[player['room']][player['facing']]
    feedback = house['feedback']

    print("""=== This Old House ===

You are in the {room} facing {facing}

straight ahead is {hd}

== Options ==
l = turn left
r = turn right
f = move forward
q = quit

"{fb}"
"What would you like to do?"
""".format(**player, hd=ahead, fb=feedback))

    return


def turn(house, player, directions):  ##JH UPDATED and USED
    """Changes direction base on user input"""

    last_index = len(directions) - 1
    dir_index = directions.index(player['facing'])

    if player['input'] == 'l':
        if dir_index == 0:
            player['facing'] = directions[last_index]
        else:
            player['facing'] = directions[dir_index-1]
    elif player['input'] == 'r':
        if dir_index < last_index:
            player['facing'] = directions[dir_index+1]
        else:
            player['facing'] = directions[0]

    house['feedback'] = 'take a look around'

    return


##JH def clean_input(input_type):
##JH     """ Cleans input based on what i """


def display_map():  ##JH UPDATED and USED
    """Clears the screen and displays map until enter is pressed"""

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


def password_challenge(house):  ##JH UPDATED and USED
    """Takes user input and compares it to argument entered"""

    os.system('cls' if os.name == 'nt' else 'clear')
    if input('\nWhat is the password? ') == house['study']['east']:
        return True
    else:
        return False


def change_rooms(player):  ##JH UPDATED and USE
    """Moves you to a new room"""

    if player['room'] == 'foyer':
        if player['facing'] == 'north':
            player['room'] = 'bathroom'
        elif player['facing'] == 'west':
            player['room'] = 'parlor'

    elif player['room'] == 'parlor':
        if player['facing'] == 'east':
            player['room'] = 'foyer'
        elif player['facing'] == 'north':
            player['room'] = 'kitchen'

    elif player['room'] == 'study':
        player['room'] = 'master bedroom'

    elif player['room'] == 'master bedroom':
        if player['facing'] == 'east':
            player['room'] = 'kitchen'
        elif player['facing'] == 'south':
            player['room'] = 'study'

    elif player['room'] == 'kitchen':
        if player['facing'] == 'south':
            player['room'] = 'parlor'
        elif player['facing'] == 'west':
            player['room'] = 'master bedroom'

    elif player['room'] == 'bathroom':
        player['room'] = 'foyer'


def forward(house, player, rooms):  ##JH UDATED and USED
    """Resonds to the users selection to move forward"""

    ahead = house[player['room']][player['facing']]

    if ahead == 'an open door':
        change_rooms(player)
        # if you make it into the bathroom
        # you win and can only go into room 1 and exit
        # your direction also changes to south
        if player['room'] == 'bathroom':
            house['feedback'] = 'You get the treasure, now leave in peace.'
            player['won'] = True
            player['facing'] = 'south'
            house['foyer']['west'] = 'a closed door'
        # if not in room five, feedback is
        # given that you are in a new room
        else:
            house['feedback'] = "You're in a new room"

    # if the door is locked and you move forward,
    # you are challenged for a password
    elif ahead == 'a locked door':
        # if you get the password right, the
        # locked door becomes an open door
        if password_challenge(house):
            house['feedback'] = 'You guessed right'
            house['foyer']['north'] = 'an open door'
        # otherwise, the door stays
        # locked and the password changes
        else:
            house['feedback'] = 'You guessed wrong. It is written anew.'
            house['study']['east'] = random_password()

    # if you see a wall, you're scolded, but given hope
    elif ahead == 'a wall':
        house['feedback'] = "You can't walk through walls yet"

    # if you see an exit, you leave the game by going forward
    elif ahead == 'the exit':
        player['input'] = 'q'

    # the door to the parlor - or rest of the
    # house - closed once you enter the bathroom
    elif ahead == 'a closed door':
        house['feedback'] = 'You have your treasure, please leave.'

    # if you see a map, you get to find where you are
    elif ahead == 'a map':
        display_map()
        house['feedback'] = "don't get lost now"

    return


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
        hud(house, player)
        # Get User input
        player['input'] = input(': ').lower()
        if player['input'] == 'l' or player['input'] == 'r':  # turning l/r
            turn(house, player, directions)
        elif player['input'] == 'f':
            forward(house, player, rooms)
        if player['input'] == 'q':  # quit if q
            break

    os.system('cls' if os.name == 'nt' else 'clear')
    if player['won']:
        print("\n\tCongradulations!!\n\tSpend it on charity, will ya?!\n")
    else:
        print('\n\tSmell you later!\n')


main()