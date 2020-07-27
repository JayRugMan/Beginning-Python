#!/usr/bin/python3                              # 1
# numberlines.py                                # 2
                                                # 3
import fileinput                                # 4
                                                # 5
for line in fileinput.input(inplace=True):      # 6
    line = line.rstrip()                        # 7
    num = fileinput.lineno()                    # 8
    print('{0:<47} # {1}'.format(line, num))    # 9
