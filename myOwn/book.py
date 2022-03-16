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
                 This designates the file that acts as the "book" in the book
                 code by using its base64 encoding. It can be any type of
                 file - .html, .img, .jpg, .mp4, etc. Keep in mind if the
                 file is too small, the entropy will be small; if the file is
                 too big, the process time and performance may be impacted.

'''
    message_help='''\
                 This is the message string to be encoded. It can be a string
                 or a plain-text file. This cannot be used with -c/--code.

'''
    code_help='''\
                 The code goes here. This can also be a file containing the
                 code in plain text. This cannot be used with -m/--message.

'''
    the_epilog='''\

notes:
  Only the following special characters will work:
    . , ' ? + - = : ! @ # $ % ^ & * /
                        
  Some special characters will encode better if a message file is \
used instead of a string on the terminal

'''

    parser = (argparse.ArgumentParser(
                  prog='book.py',
                  formatter_class=lambda prog: argparse.RawDescriptionHelpFormatter(
                      prog,indent_increment=2,max_help_position=41),
##JH                  formatter_class=lambda prog: argparse.HelpFormatter(
##JH                      prog,indent_increment=2,max_help_position=41),
##JH                  formatter_class=lambda prog: argparse.RawTextHelpFormatter(
##JH                      prog,indent_increment=2,max_help_position=41),
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
    '''Processes the book file to return a list of lines in base64 charset
    with shifted indeces and a line count (hence the "insert")'''

    with open(book, 'rb') as the_book:
        book_lst = [
            i for i in base64.encodebytes(
                the_book.read()
            ).decode('utf-8').split('\n') if len(i) != 0
        ]

    # This makes line 1 move to line 2 to be index 1
    # for later. The string is arbitrary.
    book_lst.insert(0, 'These bits are the book')
    
    return book_lst


def process_txt_file(txt_file):
    '''turns file into a string for further processing'''

    ex_msg = "doesn't look like any text is in " + \
        txt_file + \
        ". Try one with ascii text next time."

    try:
        with open(txt_file, 'r') as file:
            file_lst = [i for i in file.read().split('\n') if len(i) != 0]
    except UnicodeDecodeError:
        # if this is a non-text file, like an image, etc
        print(ex_msg)
        sys.exit(1)

    return ' '.join(file_lst)


def enrich_message(message_object, specials):
    '''Refines the message to determine if it's a sting or file, then if
    it has any special characters, which are translated to special-character
    strings so the can be encoded with base64 characters'''

    # Returns true or false depending on whether the string provided is a
    # file. Even if the user is trying to specify a file, but does not exist,
    # it will treat it as a string. Harsh, I know.
    if exists(message_object):
        message_object = process_txt_file(message_object)

    enriched_message = ''

    for char in message_object:
        if char in specials.keys():
            enriched_message += specials[char]
        else:
            enriched_message += char

    return enriched_message


def encode_message(message, special_cs, book_f):
    '''takes the book and the message and works some maigic'''
    
    message_str = enrich_message(message, special_cs)
    book_list = process_book(book_f)
    numb_of_lines = len(book_list)
    code = ''

    for character in message_str:
        while True:
            rand_line_num = secrets.randbelow(numb_of_lines)
            if character in book_list[rand_line_num] and rand_line_num != 0:
                line = ' {}'.format(book_list[rand_line_num])  # offset index
                idx = line.index(character)
                code += '{} {} '.format(rand_line_num, idx)
                break

    return code[:-1]  # because the last char is a space


def interpret_specials(message, specials):
    '''takes special characters and raw message to translate, returning them
    to normal for the final string'''

    for new, old in specials.items():
        if old in message:
            message = message.replace(old, new)

    return message


def de_the_code(code_object, book_f, special_cs):
    '''Takes numbers and book, then returns what it all means'''

    # Returns true or false depending on whether the string provided is a
    # file. If the user is trying to specify a file, but does not exist,
    # it will treat it as a string and return nothing. Harsh, I know.
    if exists(code_object):
        code_object = process_txt_file(code_object)

    book_list = process_book(book_f)
    raw_message = ''
    line_num = None
    char_num = None

    # This loop stores number pairs from a string-turned-to-list to then
    # store corresponding line and character from the book
    for item in code_object.split(' '):
        if not line_num:
            line_num = item
        else:
            char_num = item
        if line_num and char_num:
            line = ' {}'.format(book_list[ int(line_num) ])  # to offset index
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
        final_answer = encode_message(args['the_message'],
                                      special_chars,
                                      args['book_file']
                                     )
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
