#!/usr/local/bin/python3.7
# Prints a sentence in a centered "box" of correct width

# Note that the integer division operator (//) only works in python
# 2.2 and newer. In earlier versions, simply use plain division (/)

sentence = input("Sentence: ")

screen_width = 200
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

box_top_bttm = ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
box_blank = ' ' * left_margin + '|  ' + ' ' * text_width + '  |'
box_sentence = ' ' * left_margin + '|  ' + sentence + '  |'
output_string = '\n\n%s\n%s\n%s\n%s\n%s\n\n'
output_args = (box_top_bttm, box_blank, box_sentence, box_blank, box_top_bttm)

print(output_string % output_args)
