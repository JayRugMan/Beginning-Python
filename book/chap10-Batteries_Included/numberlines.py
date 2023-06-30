#!/usr/bin/python3
# numberlines.py

import fileinput

for line in fileinput.input(inplace=True, backup=".bk"):
    line = line.rstrip()
    num = fileinput.lineno()
    print('{0:<4} | {1}'.format(num, line))
