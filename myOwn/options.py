#!/usr/bin/python3

import sys
import argparse


def main():
    blahDiddy = None
    mine = (argparse.ArgumentParser(prog='options.py', description='just a test'))
    mine.add_argument('test',type=str,help='the only one')
    print(vars(mine.parse_args(blahDiddy))['test'])


if __name__ == "__main__":
    sys.exit(main())
