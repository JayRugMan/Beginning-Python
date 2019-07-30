#!/usr/local/bin/python3.7

noun_prop = 'Enter a proper noun: '
adj = 'Enter an adjective: '

values_list = []
values_list.append(input(noun_prop))
values_list.append(input(adj))
values_tuple = tuple(values_list)
sentence = 'Hello %s. %s enough for you?'

print(sentence % values_tuple)
