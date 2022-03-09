#!/usr/bin/python3
'''This script does stuff'''

import base64


with open('recordings.png', 'rb') as the_book:
    book_lst = [
      i for i in base64.encodebytes(
        the_book.read()
        ).decode('utf-8').split('\n') if len(i) != 0
    ]
book_str = '\n'.join(book_lst)

##JH https://www.tutorialspoint.com/python3/python_command_line_arguments.htm
