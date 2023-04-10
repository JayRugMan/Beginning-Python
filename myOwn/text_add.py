#! /usr/bin/env python3

ones = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine']

teens = [
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen']

tens = [
    'ten',
    'twenty',
    'thirty',
    'forty', 
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety']

magnitudes = [
    'hundred',
    'thousand',
    'million',
    'billion',
    'trillion']


def get_digit(txt_num):
    if txt_num in ones:
        the_digit = ones.index(txt_num)
    elif txt_num in teens:
        the_digit = teens.index(txt_num) + 11
    elif txt_num in tens:
        the_digit = ( tens.index(txt_num) + 1 ) * 10
    return the_digit


def get_text(dig_num):
    if 0 <= dig_num < 10:
        the_text = ones[dig_num]
    elif 10 < dig_num < 20:
        the_text = teens[int(dig_num - 11)]
    elif 9 < dig_num < 100 and (dig_num % 10) == 0:
        the_text = tens[int((dig_num / 10) - 1)]
    return the_text


def factor(the_number):
    num_str = str(the_number)
    num_len = len(num_str)
    the_zeros = (num_len - 1)
    factor_list = []
    for i in range(num_len):
        factor_list.append(int(num_str[i] + "0" * the_zeros))
        the_zeros -= 1
    return factor_list
