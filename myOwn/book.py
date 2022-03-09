#!/usr/bin/python3
'''This script does stuff'''

import base64
import sys
import getopt


def usage(error_str=None):
    '''Prints usage...'''
##JH https://www.programcreek.com/python/example/202/getopt.GetoptError
    if error_str is not None:
        print('ERROR: {}'.format(error_str))

    print('''

Usage:

-b <binary file>,
--book=<binary file>       This designates the binary file that acts as the
                           "book" in the book code and can be any type of
                           binary file, like a webpage, img, .jpg, .mp4, etc.
                           Keep in mind if the file is too small, the entropy
                           will be small; if the file is too big, the process
                           time and performance may be impacted.

-m "string",
--message="string"         This is the message string to be encoded. It can be
                           a string or a plain-text file. This cannot be used
                           with -c/--code.

-c <numbers>,
--code=<numbers>           The code goes here. This cannot be used with
                           -m/--message.

*                          Prints this helpful output


Special Characters         Only the following special characters will work:
                                  . , ' ? + - = : ! @ # $ % ^ & * /

                           Note that some special characterswill encode better
                           if a message file is used instead of a string on the
                           terminal

    ''')


def main(argv):
    '''Main event'''

    try:
        opts, arg = getopt.getopt(argv, "b:m:c:",["book=","message=","code="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-b', '--book'):
            book_file = arg
            print(book_file)
        elif opt in ('-m', '--message'):
            message = arg
            print(message)
        elif opt in ('-c', '--code'):
            code = arg
            print(code)


##JH    with open('recordings.png', 'rb') as the_book:
##JH        book_lst = [
##JH          i for i in base64.encodebytes(
##JH            the_book.read()
##JH            ).decode('utf-8').split('\n') if len(i) != 0
##JH        ]
##JH    book_str = '\n'.join(book_lst)

##JH https://www.tutorialspoint.com/python3/python_command_line_arguments.htm

if __name__ == "__main__":
    main(sys.argv[1:])
