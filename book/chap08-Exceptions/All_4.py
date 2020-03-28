#!/usr/bin/python3
try:
    1/0
except NameError:
    print('Unknown Variable')
else:
    print('That went well.')
finally:
    print('Cleaning up')
