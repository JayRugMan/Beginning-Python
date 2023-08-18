#!/usr/bin/python3

name,color = input("Hi, what is your name and fav color? ").split()
h = 'Hello'
hf = f'{h}, {name}!'

color_list = [
    'blue',
    'gold',
    'black',
    'white',
    'purple',
    'pink',
    'red',
    'yellow',
    'green',
    'orange',
    'gray',
    'grey',
    'brown'
]

if color == 'blue':
    fc = f'{color} is my favorite color, too!'
elif color in color_list:
    fc = f"Cool, I guess {color} isn't bad."
else:
    fc = f"Hmm. I didn't know {color} was a color."

print(hf)     # "Hello, <name>!"
print(fc)
