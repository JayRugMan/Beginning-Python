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


def random_password():
    """Returns a random password from a list of passwords
    depends on imported random"""

    password_list = ['sandman', 'Lockhead', 'Babling brooK', 'Santa Claus',
                     'Peanut', 'fury flurry', 'clinician', 'random PassWord']
    p_word_picker = random.randint(0, (len(password_list) - 1))
    pw = password_list[p_word_picker]
    return pw


def build_house():
    """Creates the house dictionary, a dictionary on how the rooms connect,
    and a compass dictionary defining directions right or left of oneanother"""

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
            'east': random_password(),
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
    infrastructure = {  # Used for changing rooms
        'foyer': {
            'north': 'bathroom',
            'west': 'parlor'},
        'parlor': {
            'east': 'foyer',
            'north': 'kitchen'},
        'study': {'north': 'master bedroom'},
        'master bedroom': {
            'east': 'kitchen',
            'south': 'study'},
        'kitchen': {
            'south': 'parlor',
            'west': 'master bedroom'},
        'bathroom': {'south': 'foyer'}
    }
    compass = {  # used for changing directions and defining player
        'l': {
            'north': 'west',
            'west': 'south',
            'south': 'east',
            'east': 'north'},
        'r': {
            'north': 'east',
            'east': 'south',
            'south': 'west',
            'west': 'north'}
    }
    options = {  # used for dynamic heads up display options menu
        'q': ' quit',
        'f': ' move forward',
        'r': ' turn right',
        'l': ' turn left'
    }
    actions = {  # used to update options dictinary per what's ahead
        'a locked door': 'unlock door',
        'a map': 'look at map',
        'the exit': 'exit',
        'an open door': 'walk through',
        'a wall': 'move forward',
        'a closed door': 'try door',
        house['study']['east']: 'move forward'
    }
    return house, infrastructure, compass, options, actions


def define_player(infrastructure, compass):
    """Sets initial room and direction randomly"""

    directions = [key for key in compass['r']]
    rooms = [rm for rm in infrastructure]
    room = rooms[random.randint(0, 4)]  # does not include locked room
    direction = directions[random.randint(0, 3)]
    player = {
        'room': room,
        'facing': direction,
        'won': 'no'
    }
    return player


def hud(house, player, options, actions):
    """Prints HUD with which room your in, which direction you're facing, What
    is straight ahead, and what the feedback is from the host of the house"""

    os.system('cls' if os.name == 'nt' else 'clear')  # clear screen
    ahead = house[player['room']][player['facing']]
    # Hackish, for now - if pw is updated, new actions key/value needed
    actions[house['study']['east']] = 'move forward'
    # Option for f changed depending on what's ahead
    options['f'] = actions[ahead]
    feedback = house['feedback']
    output_list = [
        '=== This Old House ===',
        '',
        'You are in the {room} facing {facing}'.format(**player),
        '',
        'straight ahead is {}'.format(ahead),
        '',
        '===== Options =====',  # options will be inserted below this line
        '',
        '"{}"'.format(feedback),
        '"What would you like to do?"',
        ''
    ]
    opt_tbl = '{0:<2}{1:.>17}'  # makes options box 17 wide in justified format
    # inserts justified table into output list
    for input, action in options.items():
        output_list.insert(7, opt_tbl.format(input, action))
    for line in output_list:  # Prints each line centered from output_list
        print('{0:^57}'.format(line))
    return


def display_map():
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
    prompt = 'Hit ENTER to close map.'
    input('{:^57}'.format(prompt))
    return


def password_challenge(house):
    """Takes user input and compares it to argument entered"""

    os.system('cls' if os.name == 'nt' else 'clear')
    if input('\nWhat is the password? ') == house['study']['east']:
        return True
    else:
        return False


def forward(house, player, infrastructure):
    """Resonds to the users selection to move forward"""

    ahead = house[player['room']][player['facing']]
    if ahead == 'an open door':
        # updates player's room based on infrastructure dictionary
        player['room'] = infrastructure[player['room']][player['facing']]
        # if you make it into the bathroom
        # you win and can only go into room 1 and exit
        # your direction also changes to south
        if player['room'] == 'bathroom':
            house['feedback'] = 'You get the treasure, now leave in peace.'
            player['won'] = 'yes'
            player['facing'] = 'south'
            house['foyer']['west'] = 'a closed door'
        # if not in the bathroom, feedback is
        # given that you are in a new room
        else:
            house['feedback'] = "You're in a new room"
    # if the door is locked and you choose to unlock it,
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


def player_interactions(house, player, infrastructure, compass):
    """Defines the player's interacions with the game"""

    player['input'] = input(': ').lower()
    if player['input'] == 'l' or player['input'] == 'r':  # turning l/r
        # player will face new direction based on compass dictionary
        player['facing'] = compass[player['input']][player['facing']]
        house['feedback'] = 'take a look around'
    elif player['input'] == 'f':
        forward(house, player, infrastructure)
    return


def main():
    'Main Function'

    # Build environmental dictionaries necessary for gameplay
    house, infrastructure, compass, options, actions = build_house()
    # Initialize player with start room, direction, and "won" status
    player = define_player(infrastructure, compass)
    # Defines formatting and phrases for exiting comments
    centered_output = '\n{:^57}\n'
    closing_output = {
        'yes': 'Congradulations!! Spend it on charity, will ya?!',
        'no': 'Smell ya later!'
    }
    # Enter gameplay loop
    while True:
        # Heads Up Display
        hud(house, player, options, actions)
        # Get player interaction
        player_interactions(house, player, infrastructure, compass)
        if player['input'] == 'q':  # quit if q
            break
    os.system('cls' if os.name == 'nt' else 'clear')
    # If player won is yes, closing output changes
    print(centered_output.format(closing_output[player['won']]))


main()
