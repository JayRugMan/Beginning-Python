#!/usr/bin/python3

import sys
import re


class bcolors:
    IP = '\033[34m'
    PASS = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'


def is_ip(string):
    if not re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", string):
        return False
    bytes = string.split(".")
    for ip_byte in bytes:
        try:
            if int(ip_byte) < 0 or int(ip_byte) > 255:
                return False
        except ValueError:
            return False
    return True


def main():
    # The main event

    test_string = sys.argv[1]

    if is_ip(test_string):
        results = '{}{}{}: {}valid IP address{}'.format(bcolors.IP, test_string, bcolors.ENDC, bcolors.PASS, bcolors.ENDC)
    else:
        results = '{}{}{}: {}invalid IP address{}'.format(bcolors.IP, test_string, bcolors.ENDC, bcolors.FAIL, bcolors.ENDC)

    print(results)


if __name__ == "__main__":
    
    sys.exit(main())
