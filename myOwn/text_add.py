#! /usr/bin/env python3


from itertools import tee

from cairo import TEXT_CLUSTER_FLAG_BACKWARD


class the_number():
    def __init__(self):
        self.ones = [
            'zero',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine'
        ]
        self.teens = [
            'eleven',
            'twelve',
            'thirteen',
            'fourteen',
            'fifteen',
            'sixteen',
            'seventeen',
            'eighteen',
            'nineteen'
        ]
        self.tens = [
            'ten',
            'twenty',
            'thirty',
            'forty', 
            'fifty',
            'sixty',
            'seventy',
            'eighty',
            'ninety'
        ]
        self.magnitudes = [
            'hundred',
            'thousand',
            'million',
            'billion',
            'trillion'
        ]
    def factor(self, the_number):
        num_str = str(the_number)
        factor_list = list(map(int, list(num_str)))
        list_len = len(factor_list)
        num_list = []
        for i in range(list_len):
            if i == (list_len - 2) and 10 < int(f"{factor_list[i]}{factor_list[i+1]}") < 20:
                num_list.append( int(f"{factor_list[i]}{factor_list[i+1]}") )
                break
            else:
                num_list.append(int(factor_list[i]))
        return num_list
    def get_digit(self, txt_num):
        if txt_num in self.ones:
            the_digit = self.ones.index(txt_num)
        elif txt_num in self.teens:
            the_digit = self.teens.index(txt_num) + 11
        elif txt_num in self.tens:
            the_digit = ( self.tens.index(txt_num) + 1 ) * 10
        return the_digit
    def get_text(self, dig_num):
        factored_num = self.factor(dig_num)
        place_count = len(''.join(map(str, factored_num)))
        text_num = []
        for factor in factored_num:
            if place_count >= 3:
                text_num.append(f"{self.ones[factor]}-{self.magnitudes[ (place_count-3) ]}")


            if 0 <= factor < 10:
                text_num.append(self.ones[factor])
            elif 10 < factor < 20:
                text_num.append(self.teens[int(factor - 11)])
            elif 9 < factor < 100 and (factor % 10) == 0:
                text_num.append(self.tens[int((factor / 10) - 1)])
        return '-'.join(text_num)
