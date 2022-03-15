#!/usr/bin/python3
'''This script does stuff'''

import base64
import sys
import argparse
import secrets


def main():
    the_description='Using a file as a "book," a message can be processed into a code or vise-versa.'
    help_help = '''\
                 You get this helpful message before exiting
 
'''
    book_help = '''\
                 This designates the binary file that acts as the
                 "book" in the book code and can be any type of
                 binary file, like a webpage, img, .jpg, .mp4, etc.
                 Keep in mind if the file is too small, the entropy
                 will be small; if the file is too big, the process
                 time and performance may be impacted.
 
'''
    message_help='''\
                 This is the message string to be encoded. It can be
                 a string or a plain-text file. This cannot be used
                 with -c/--code.
 
'''
    code_help='''\
                 The code goes here. This cannot be used with
                 -m/--message.
 
'''
    the_epilog='''\

  Special Characters -                   Only the following special characters will work:
                                           ---  . , ' ? + - = : ! @ # $ % ^ & * /  ---
                                         
                                         Note that some special characters will encode better
                                         if a message file is used instead of a string on the
                                         terminal
 
'''
        
    parser = (argparse.ArgumentParser(
                  prog='book.py',
                  formatter_class=lambda prog: argparse.HelpFormatter(
                      prog,max_help_position=50),
##JH                  formatter_class=argparse.RawTextHelpFormatter,
                  add_help=False,
                  description=the_description,
                  epilog=the_epilog
                  )
             )
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('-h', '--help',
                        action='help',
                        default=argparse.SUPPRESS,
                        help=help_help
                       )
    parser.add_argument('-b', '--book',
                        required=True,
                        dest='book_file',
                        type=str,
                        help=book_help
                       )
    group.add_argument('-m', '--message',
                        dest='the_message',
                        type=str,
                        help=message_help
                       )
    group.add_argument('-c', '--code',
                        dest='the_code',
                        type=str,
                        help=code_help
                       )
    
    args = vars(parser.parse_args())
    ##JHimport getopt
    ##JH
    ##JH
    ##JHdef usage(error_str=None):
    ##JH    '''Prints usage...'''
    ##JH##JH https://www.programcreek.com/python/example/202/getopt.GetoptError
    ##JH    if error_str is not None:
    ##JH        print('ERROR: {}'.format(error_str))
    ##JH
    ##JH    print('''
    ##JH
    ##JHUsage:
    ##JH
    ##JH-b <binary file>,
    ##JH--book=<binary file>       This designates the binary file that acts as the
    ##JH                           "book" in the book code and can be any type of
    ##JH                           binary file, like a webpage, img, .jpg, .mp4, etc.
    ##JH                           Keep in mind if the file is too small, the entropy
    ##JH                           will be small; if the file is too big, the process
    ##JH                           time and performance may be impacted.
    ##JH
    ##JH-m "string",
    ##JH--message="string"         This is the message string to be encoded. It can be
    ##JH                           a string or a plain-text file. This cannot be used
    ##JH                           with -c/--code.
    ##JH
    ##JH-c <numbers>,
    ##JH--code=<numbers>           The code goes here. This cannot be used with
    ##JH                           -m/--message.
    ##JH
    ##JH*                          Prints this helpful output
    ##JH
    ##JH
    ##JHSpecial Characters         Only the following special characters will work:
    ##JH                                  . , ' ? + - = : ! @ # $ % ^ & * /
    ##JH
    ##JH                           Note that some special characterswill encode better
    ##JH                           if a message file is used instead of a string on the
    ##JH                           terminal
    ##JH
    ##JH    ''')
    ##JH
    ##JH
    ##JHdef main(argv):
    ##JH    '''Main event'''
    ##JH
    ##JH    try:
    ##JH        opts, arg = getopt.getopt(argv, "b:m:c:",["book=","message=","code="])
    ##JH    except getopt.GetoptError:
    ##JH        usage()
    ##JH        sys.exit(2)
    ##JH
    ##JH    for opt, arg in opts:
    ##JH        if opt in ('-b', '--book'):
    ##JH            book_file = arg
    ##JH            print(book_file)
    ##JH        elif opt in ('-m', '--message'):
    ##JH            message = arg
    ##JH            print(message)
    ##JH        elif opt in ('-c', '--code'):
    ##JH            code = arg
    ##JH            print(code)
    
    with open(args['book_file'], 'rb') as the_book:
        book_lst = [
          i for i in base64.encodebytes(
            the_book.read()
            ).decode('utf-8').split('\n') if len(i) != 0
        ]
    book_str = '\n'.join(book_lst)
    num_of_lines = len(book_lst)
    book_lst.insert(0, 'These bits are the book')
    
    print('file used as book: {book_file}\nmessage: {the_message}'.format(**args))


if __name__ == "__main__":
    sys.exit(main())
