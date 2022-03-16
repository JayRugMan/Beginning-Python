#!/usr/bin/python3
'''This script does stuff'''

import base64
import sys
import argparse
import secrets
from os.path import exists


def get_args(argv=None):
    '''Uses argparse to get input'''

    the_description='Using a file as a "book," a message can ' \
        'be processed into a code or vise-versa.'
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

    return vars(parser.parse_args(argv))


def process_book(book):
    '''Processes the book file to return a list of lines with shifted
    indexes and a line count (hence the "insert")'''

    with open(book, 'rb') as the_book:
        book_lst = [
            i for i in base64.encodebytes(
                the_book.read()
            ).decode('utf-8').split('\n') if len(i) != 0
        ]

    num_of_lines = len(book_lst)
    book_lst.insert(0, 'These bits are the book')
    
    return num_of_lines, book_lst


def process_message_file(message_file):
    '''turns file into a string for further processing'''

    ex_msg = "doesn't look like a message is in " + \
        message_file + \
        "Try one with ascii text next time."

    try:
        with open(message_file, 'r') as file:
            file_lst = [i for i in file.read().split('\n') if len(i) != 0]
    except UnicodeDecodeError:
        # if this is a non-text file, like an image, etc
        print(ex_msg)
        sys.exit(1)

    return ' '.join(file_lst)


def process_message(raw_message, specials):
    '''Processes the message to determine if it's a sting or file, then if
    it has any special characters, which are translated to special-character
    strings so the can be encoded with base64 characters'''

    # Returns true or false depending on whether the string provided is a
    # file. Even if the user is trying to specify a file, but does not exist,
    # it will treat it as a string. Harsh, I know.
    if exists(raw_message):
        raw_message = process_message_file(raw_message)

    final_message = ''
    for char in raw_message:
        if char in specials.keys():
            final_message += specials[char]
        else:
            final_message += char

    return final_message


def encode_message(book_f, message):
    '''takes the book and the message and works some maigic'''
    
    numb_of_lines, book_list = process_book(book_f)
    code = ''
    for character in message:
        while True:
            random_line_num = secrets.randbelow(numb_of_lines)
            if character in book_list[random_line_num]:
                line = ' {}'.format(book_list[random_line_num])  # offset index
                idx = line.index(character)
                code += '{} {} '.format(random_line_num, idx)
                break

    return code[:-1]  # because the last char is a space


def interpret_specials(message, specials):
    '''takes special characters and raw message to translate, returning them
    to normal for the final string'''

    for new, old in specials.items():
        if old in message:
            message = message.replace(old, new)

    return message


def de_the_code(code, book_f, special_cs):
    '''Takes numbers and book, then returns what it all means'''

    numb_of_lines, book_list = process_book(book_f)
    raw_message = ''
    line_num = None
    char_num = None

    for item in code.split(' '):
        if not line_num:
            line_num = item
        else:
            char_num = item
        if line_num and char_num:
            line = ' {}'.format(book_list[ int(line_num) ])
            raw_message += line[ int(char_num) ]
            line_num = None
            char_num = None

    return interpret_specials(raw_message, special_cs)


def main():
    '''The Main Event'''

    options = None
    special_chars = {
        '.': "XSPp",
        ',': "XSPc",
        "'": "XSPa",
        '?': "XSPq",
        '+': "XSPl",
        '-': "XSPd",
        '=': "XSPe",
        ':': "XSPo",
        '!': "XSP1",
        '@': "XSP2",
        '#': "XSP3",
        '$': "XSP4",
        '%': "XSP5",
        '^': "XSP6",
        '&': "XSP7",
        '*': "XSP8",
        ' ': "+"
    }

    args = get_args(options)

    if args['the_message']:
        message_string = process_message(args['the_message'], special_chars)
        final_answer = encode_message(args['book_file'], message_string)
    elif args['the_code']:
        final_message = de_the_code(args['the_code'],
                                   args['book_file'],
                                   special_chars
                                  )
        final_answer = 'Message:\n{}\n'.format(final_message)
    else:
        final_answer = 'Oppsy... how did this happen?'

    print(final_answer)


if __name__ == "__main__":
    sys.exit(main())
