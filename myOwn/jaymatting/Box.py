# Box.py

from jaymatting.Line_Characters import Boxes


class Box(Boxes):
    '''Constructs a box around the input - takes dictionary of
    strings, where the key contains either center, right, or
    left for the justification of the string in the dictionary's
    value'''

    def __init__(self):
        super().__init__()

    def get_width(self, innardsDict):
        '''Gets the longest line of the string'''
        longest = 0
        for value in innardsDict.values():
            innardsLst = value.split('\n')
            for item in innardsLst:
                if len(item) > longest:
                    longest = len(item)
        return longest

    def fill_box(self, innardsDict, width):
        '''Either centers, or justifies left or right
        values based on keys and returns a single string
        combining each section formatted properly'''
        strList = []
        for key, value in innardsDict.items():
            if 'center' in key:
                s = '{0}{1:^{w}}{0}'
            elif 'right' in key:
                s = '{0}{1:>{w}}{0}'
            elif 'left' in key:
                s = '{0}{1:<{w}}{0}'
            for line in value.split('\n'):
                strList.append(s.format(self.edges, line, w=width))
        return '\n'.join(strList)

    def put_in_box(self, innardsDict):
        '''Puts the specified string into a box recieves a dict of strings,
        separated based on number of differing formatting - centered, right
        or left justified, the format(s) being the key(s)'''
        width = self.get_width(innardsDict) + 2
        top = '{}{}{}'.format(self.cornerTL, self.tpBtm*(width), self.cornerTR)
        bottom = '{}{}{}'.format(self.cornerBL, self.tpBtm*(width),
                                 self.cornerBR)
        fString = '{t}{nl}{guts}{nl}{b}'
        boxedStr = fString.format(t=top, nl='\n', b=bottom,
                                  guts=self.fill_box(innardsDict, width))
        return boxedStr
