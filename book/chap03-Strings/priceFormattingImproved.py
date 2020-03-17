#!/usr/bin/python3
# Print a formatted price list with a given width


def longestL(lst):
    # gets the longest item from list and adds a buffer of
    # 9 (2 for each edge, which is 4, then 5 for min middle
    # padding). This value is returned as an integer

    list_len = 0
    # Iterates through the provided list's sublists
    for slist in lst:
        item1_len = len(slist[0])
        if type(slist[1]) is str:
            item2_len = len(slist[1])
        else:
            item2_len = len('{:.2f}'.format(slist[1]))
        total_len_P9 = item1_len + item2_len + 9
        if total_len_P9 > list_len:
            list_len = int(total_len_P9)
    return list_len


def headerString(lst, wdth, edg):
    # Returns formatted header string

    h1 = '{0:<2}{1}'.format(edg, lst[0][0])
    h2 = '{1}{0:>2}'.format(edg, lst[0][1])
    gap = wdth - len(h2)
    header_format = '{0:<{gap}}{1}'
    final_str = header_format.format(h1, h2, gap=gap)
    return final_str


def listStrings(lst, wdth, edg):
    # Generates list strings with buffered side
    # borders and buffered Dollar-signed prices

    symbol = '$'
    items_format = '{0:<{gap}}{1}'
    for slist in lst[1:]:
        item = '{0:<2}{1}'.format(edg, slist[0])
        price = '{smbl}{1:{buff}.2f}{0:>2}'.format(edg, slist[1],
                                                   smbl=symbol, buff=6)
        gap = wdth - len(price)
        yield items_format.format(item, price, gap=gap)


def drawTable(lst, wdth):
    # Draws the table

    w = wdth - 1  # minus one for the right edge
    border1 = '='
    border2 = '-'
    edge1 = '+'
    edge2 = '|'
    print('{edge:{fill}<{w}}{edge}'.format(edge=edge1, fill=border1, w=w))
    print(headerString(lst, wdth, edge2))
    print('{edge:{fill}<{w}}{edge}'.format(edge=edge1, fill=border2, w=w))
    for line in listStrings(lst, wdth, edge2):
        print(line)
    print('{edge:{fill}<{w}}{edge}'.format(edge=edge1, fill=border1, w=w))


def main():
    # Main Function

    # First sub-list is the header info
    raw_list = [['Item', 'Price'],
                ['Apples', 0.4],
                ['Pears', 0.5],
                ['Cantaloupes', 1.92],
                ['Dried Apples', 8],
                ['Prunes (4 lbs.)', 12],
                ['Carmel-Apple carmels', 10.3],
                ['Skewers', 3.80]]
    min_width = longestL(raw_list)
    width = int(input(
        'Please enter width (min width is {}): '.format(min_width)
        ))
    if width < min_width:
        width = min_width
    drawTable(raw_list, width)


main()
