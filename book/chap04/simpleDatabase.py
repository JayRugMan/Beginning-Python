#!/usr/local/bin/python3.7
# playing around with Dictionaries
# A simple Database

# A dictionary with person names as keys. Each person is represented as
# another dictionary with the keys 'phone' and 'addr' referring to thier phone
# number and address, respctively

people = {

    'Alice': {
        'phone': '2341',
        'addr': 'Foo Drive 23'
    },

    'Beth': {
        'phone': '9102',
        'addr': 'Bar Street 42'
    },

    'Cecil': {
        'phone': '3158',
        'addr': 'Baz Avenue 90'
    }

}

# Description labels for the phone number and address. These will be used
# when printing the output.
labels = {
    'phone': 'phone extension',
    'addr': 'address'
}

name = input('Name: ')

# Are we looking for a phone number or address?
request = input('Phone number (p) or address (a)? ')

# Match request to key
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

# Only try to print information if the name is a valid key in
# our dictionary
if name in people:
    print("{}'s {} is {}.".format(name, labels[key], people[name][key]))
