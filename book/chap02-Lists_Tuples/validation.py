#!/usr/bin/python3
# Check user name and PIN code

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

username = input('User Name: ')
pin = input('PIN Code: ')

if [username, pin] in database:
    print('You are wonderful!')
else:
    print('You smell bad!')
