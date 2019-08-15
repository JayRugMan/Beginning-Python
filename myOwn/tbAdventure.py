#!/bin/python
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
def random_password():
    # takes no arguments
    # returns a random password from a list of passwords
    # depends on imported random
    
    password_list = ['sandman', 'Lockhead', 'Babling brooK', 
                    'Santa Claus', 'Peanut', 'fury flurry', 
                    'clinician', 'random PassWord']
    
    p_word_picker = random.randint(0,(len(password_list) - 1))
    pw = password_list[p_word_picker]
    
    return pw


# Takes user input and compares it to argument entered
def password_challenge(pw):
    # takes "password"
    # returns true or false
    # depends on imported os
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    user_guess = raw_input('\nWhat is the password? ')
    
    if user_guess == pw:
        return True
    
    else:
        return False


# Generates each room, with a dictionary for each wall of the room
def build_house():
    # also creates the password and writes it on the wall
    # takes in no arguments
    # returns dictionary house, with defined rooms
    # returns room_names
    # depends on random_password()

    str_password = random_password()
    
    # Foyer
    room_0 = {'north': 'a locked door', 
             'east': 'a map', 
             'south': 'the exit', 
             'west': 'an open door'}
    
    # Parlor
    room_1 = {'north': 'an open door', 
             'east': 'an open door', 
             'south': 'a wall', 
             'west': 'a wall'}
    
    # Study
    room_2 = {'north': 'an open door', 
             'east': str_password, 
             'south': 'a wall', 
             'west': 'a wall'}
    
    # Master Bedroom
    room_3 = {'north': 'a wall', 
             'east': 'an open door', 
             'south': 'an open door', 
             'west': 'a wall'}
    
    # Kitchen
    room_4 = {'north': 'a map', 
             'east': 'a wall', 
             'south': 'an open door', 
             'west': 'an open door'}
    
    # Bathroom
    room_5 = {'north': 'a wall', 
             'east': 'a wall', 
             'south': 'an open door', 
             'west': 'a wall'}
    
    list_house = [room_0, room_1, room_2, 
            room_3, room_4, room_5]
    
    list_room_names = ['foyer', 'parlor', 
                 'study', 'master bedroom', 
                 'kitchen', 'bathroom']
    
    return list_house, list_room_names


# Initializes arguments
def initialize_args():
    # takes no arguments
    # returns:
    #   directions
    #   facing_which_direction
    #   in_which_room
    #   house
    #   room_names
    #   what_you_see
    #   feedback
    #   user_input
    #   won
    # depends on build_house()

    directions = ['north', 'east', 
                 'south', 'west']
    
    # JH facing_which_direction = 0
    # JH in_which_room = 0
    
    # randomly selects the initial direction
    facing_which_direction = random.randint(0, 3)
    # randomly selects the initial room, other than bathroom
    in_which_room = random.randint(0, 4)
    
    house, room_names = build_house()
    password = house[2]['east']
    
    what_you_see = house[
        in_which_room][
        directions[
        facing_which_direction]]
    
    feedback = 'Welcome to my old house.'
    
    user_input = ''
    
    won = False
    
    return (directions, facing_which_direction, 
        in_which_room, house, room_names, password, 
        what_you_see, feedback, user_input, won)


# Displays the main screen and returns user input
def main_display(
        list_room_names, int_in_which_room, 
        list_directions, int_facing_which_direction, 
        str_what_you_see, str_feedback):
    # takes arguments to display:
    #   current room - room_names
    #   the direction you're facing - in_which_room
    #   What is straight ahead - directions
    #   and the current feedback - facing_which_direction
    # returns nothing other than screen output - what_you_see
    # Depends on imported os
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(
"""=== The House ===

current room: %s
direction you are facing: %s

straight ahead is %s

== Options ==
l = turn left
r = turn right
f = move forward
q = quit

"%s"
"What would you like to do?"
""" % (
    list_room_names[int_in_which_room], 
    list_directions[int_facing_which_direction], 
    str_what_you_see, 
    str_feedback))
    
    str_user_input = raw_input(': ')
    str_user_input = str_user_input.lower()
    return str_user_input


# Clears the screen and displays map until enter is pressed
def display_map():
    # no arguments taken or returned
    # depends on imported os
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(
"""                 === MAP of my house ===

                         -NORTH-  
                         
  +----------------+--------M-------+-----------------+ 
| |                |                |                 | |
E | master bedroom D     kitchen    |    bathroom     | W
A |                |                |                 | E
S +--------D-------+--------D-------+--------D--------+ S
T |                |                |                 | T
| |     study      |     parlor     D      foyer      M |
  |                |                |                 | 
  +----------------+----------------+--------E--------+ 
  
                        -SOUTH-
""")
    
    raw_input("\t      hit ENTER once you're done")

    
# changes directions left, or minuses from int_old_direction
# changes directions right, or adds to int_old_direction
def turning(str_user_input, int_old_direction, list_directions):
    # takes arguments for old direction and directions list
    # returns the new direction
    # no external dependancies
    
    end_of_list = len(list_directions) - 1
    
    if str_user_input == 'l':    
        if int_old_direction == 0:
            new_direction = end_of_list
        else:
            new_direction = int_old_direction - 1
    
    elif str_user_input == 'r':
        if int_old_direction < end_of_list:
            new_direction = int_old_direction + 1
        else:
            new_direction = 0

    str_feedback = 'take a look around'
    return new_direction, str_feedback

        
# Function for moving forward
def forward(
        str_what_you_see, int_in_which_room, str_feedback, 
        bul_won, int_facing_which_direction, str_house_0_west, 
        str_house_0_north, str_password, str_house_2_east, 
        str_user_input):
    
    # takes arguments:
    #   what_you_see
    #   in_which_room
    #   facing_which_direction
    #   password
    # returns arguments:
    #   int_in_which_room
    #   str_feedback
    #   bul_won
    #   int_facing_which_direction
    #   str_house_0_west
    #   str_house_0_north
    #   str_password
    #   str_house_2_east
    #   str_user_input
    # Depends on :
    #   change_rooms()
    #   password_challenge()
    #   display_map()
    
    # if the door is open, you change rooms
    if str_what_you_see == 'an open door':
        int_in_which_room = change_rooms(
            int_in_which_room, int_facing_which_direction)
        
        # if you make it into room 5 (bathroom), 
        # you win and can only go into room 1 and exit
        # your direction also changes to south
        if int_in_which_room == 5:
            str_feedback = 'You get the treasure, now leave in peace.'
            bul_won = True
            int_facing_which_direction = 2
            str_house_0_west = 'a closed door'
        
        # if not in room five, feedback is 
        # given that you are in a new room
        else:
            str_feedback = "You're in a new room"
    
    # if the door is locked and you move forward, 
    # you are challenged for a password
    elif str_what_you_see == 'a locked door':
        
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
    elif str_what_you_see == 'a wall':
        str_feedback = "You can't walk through walls yet"
    
    # if you see an exit, you leave the game by going forward
    elif str_what_you_see == 'the exit':
        str_user_input = 'q'
    
    # the door to the parlor - or rest of the 
    # house - closed once you enter the bathroom
    elif str_what_you_see == 'a closed door':
        str_feedback = 'You have your treasure, please leave.'
    
    # if you see a map, you get to find where you are
    elif str_what_you_see == 'a map':
                display_map()
                str_feedback = "don't get lost now"

    return (int_in_which_room, str_feedback, 
        bul_won, int_facing_which_direction, 
        str_house_0_west, str_house_0_north, 
        str_password, str_house_2_east, 
        str_user_input)


# moves you to a new room
def change_rooms(int_old_room, int_facing_which_direction):
    # takes interger argument for old room and direction
    # returns new room
    # This is manually configured based on the structure and 
    # layout of the house defined in build_house()
    
    # if you were in the foyer
    if int_old_room == 0:
        
        if int_facing_which_direction == 0: # and if you are facing north
            new_room = 5 # you will enter the bathroom
        
        elif int_facing_which_direction == 3: # and if you are facing west
            new_room = 1 # you will enter the parlor
    
    # if you are in the parlor
    elif int_old_room == 1:
        
        if int_facing_which_direction == 1: # and if you are facing east
            new_room = 0 # you will enter the foyer
        
        elif int_facing_which_direction == 0: # and if you are facing north
            new_room = 4 # you will enter the kitchen
    
    # if you are in the study
    elif int_old_room == 2:
        new_room = 3 # you will enter the master bedroom
    
    # if you are in the master bedroom
    elif int_old_room == 3:
        
        if int_facing_which_direction == 1: # and if you are facing east
            new_room = 4 # you will enter the kitchen
        
        elif int_facing_which_direction == 2: # and if you are facing south 
            new_room = 2 # you will enter the study
    
    # if you are in the kitchen
    elif int_old_room == 4:
        
        if int_facing_which_direction == 2: # and if you are facing south
            new_room = 1 # you will enter the parlor
        
        elif int_facing_which_direction == 3: # and if you are facing west
            new_room = 3 # you will enter the master bedroom
    
    # if you are in the bathroom
    elif int_old_room == 5:
        new_room = 0 # you will enter the foyer
    
    return new_room


# Main function
def main():
    
    # call function to initialize the following arguments
    (directions, facing_which_direction, in_which_room, 
    house, room_names, password, what_you_see, feedback, 
    user_input, won) = initialize_args()
    
    while(user_input != 'q'):
                
        user_input = main_display(room_names, in_which_room, 
                    directions, facing_which_direction, 
                    what_you_see, feedback)
        
        if user_input == 'l' or user_input == 'r':
            # the fucntion to turn is called 
            facing_which_direction, feedback = turning(
                user_input, facing_which_direction, 
                directions)
        
        elif user_input == 'f':
            
            (in_which_room, feedback, won, facing_which_direction, 
                house[0]['west'], house[0]['north'], password, 
                house[2]['east'], user_input
                ) = forward(what_you_see, in_which_room, 
                           feedback, won, facing_which_direction, 
                           house[0]['west'], house[0]['north'], 
                           password, house[2]['east'], user_input)

        what_you_see = house[
            in_which_room][
            directions[
            facing_which_direction]]
    
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if won:
        print("\n\tCongradulations!!\n\tSpend it on charity, will ya?!\n")
    
    else:
        print('\n\tSmell you later!\n')
  

main()
