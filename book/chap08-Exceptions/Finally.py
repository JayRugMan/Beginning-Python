#!/usr/bin/python3
x = None
try:
    x = 1/0
finally:
    print('Cleaning up...')
    del x
