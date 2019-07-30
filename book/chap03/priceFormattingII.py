#!/usr/local/bin/python3.7
# Print a formatted price list with a given width

width = int(input('Please enter width (min is 7): '))

price_width = 7
if width < price_width:
    width = price_width

item_width = width - price_width

header_format = '{0:<{iw}}{1:>{pw}}'
format = '{0:<{iw}}{1:>{pw}.2f}'

print('=' * width)

print(header_format.format('Item', 'Price', iw=item_width, pw=price_width))

print('-' * width)

print(format.format('Apples', 0.4, iw=item_width, pw=price_width))
print(format.format('Pears', 0.5, iw=item_width, pw=price_width))
print(format.format('Cantaloupes', 1.92, iw=item_width, pw=price_width))
print(format.format('Dried Apples', 8, iw=item_width, pw=price_width))
print(format.format('Prunes (4 lbs.)', 12, iw=item_width, pw=price_width))

print('=' * width)
