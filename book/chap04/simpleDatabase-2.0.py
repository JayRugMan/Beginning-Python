#!/usr/local/bin/python3.7
# Another simple database, but this one uses the get() method

# A dictionary of People and their info
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
    },

    'Jason': {
        'phone': '255',
        'addr': 'Westbank Street'
    }

}

# A dictionary to translate coded labels to spoken English
labels = {
    'phone': 'phone extension',
    'addr': 'address'
}

# Get the name
name = input('Name: ')

# Are we looking for the address or extension
request = input('Phone extenstion (e) or address (a)? ')

# Correct-key check
key = request  # In case the request is neither 'e' or 'a'
if request == 'e':
    key = 'phone'
if request == 'a':
    key = 'addr'

# Using get to provide default values
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print("{}'s {} is {}".format(name, label, result))
