#!/usr/bin/python3


class SAP_Basics:
    ''' Set constants for Saponification Values
    based on Potassium Hydroxide (KOH)
    source source https://www.fromnaturewithlove.com/resources/sapon.asp
    Basic SAP value per oil - more can be added'''

    def __init__(self):
        self.pig = 193
        self.lard = 194.60420115
        self.coconut = 258
        self.castor = 181
        self.ghee = 220


class Base_Ratios:
    '''Na base ratio based on Na molecular wieght devided by K molecular weight
    or 39.997 g/mol divided by 56.106 g/mol'''

    def __init__(self):
        self.naoh = 1402.755
        self.koh = 1000


class Prompts:
    '''List of prompts to be used when getting input'''

    def __init__(self):
        oilList = ' '.join(list(SAP_Basics().__dict__.keys()))
        self.oil = 'Type of oil ({}): '.format(oilList)
        self.oilAmnt = 'How many grams: '
        self.base = 'Type of base (NaOH KOH): '


class Final_Values():
    '''Class to keep the final values for output and calculate output.
    This calculates lye amounts for oil provided. The SAP value is the
    average amount of potassium Hydroxide (KOH) in micrograms needed
    to saponify the specified oil.'''

    def __init__(self, oil, amount, base):
        # solution contant or solCon is to achieve lye/water ratio of 35%:65%
        solCon = 0.35
        self.oil = oil
        self.oilAmnt = amount

        if base == 'naoh':
            self.baseFull = 'sodium hydroxide'
        elif base == 'koh':
            self.baseFull = 'potassium hydroxide'

        self.sapV = getattr(SAP_Basics(), oil)/getattr(Base_Ratios(), base)
        # Calcluate amount of Lye based on amount of oil(fat) and Sap value
        # (Amount of Fat) x (Saponification Value of the Fat) = (Amount of Lye)
        lyeAmnt = amount * self.sapV
        waterAmnt = lyeAmnt*(1/solCon - 1)
        # calculate lye 100, 99 98 97 96 95 94 93 92 91 and 90 percent
        # and puts it into list of dictionaries under attribute 'percLst'
        self.percLst = []
        for num in range(11):
            self.percLst.append({'lye': lyeAmnt*((100-num)*0.01)})
            self.percLst[num]['water'] = waterAmnt*((100-num)*0.01)


class Line_Characters:
    '''Characters for box and table'''

    def __init__(self):
        self.tpBtm = '━'
        self.cornerTL = '┏'
        self.cornerTR = '┓'
        self.cornerBR = '┛'
        self.cornerBL = '┗'
        self.edges = '┃'
        self.tblCross = '┼'
        self.tblTop = '─'
        self.tblEdges = '│'


class Table(Line_Characters):
    '''Builds table object'''

    def __init__(self, final):
        super().__init__()
        numOfRows = len(final.percLst)
        self.colmnW = [9, 11, 12]
        headList = ['percent', 'lye (g)', 'water (ml)']
        hrzBrdr = []
        for i in self.colmnW:
            hrzBrdr.append(self.tblTop*i)
        self.separators = [self.tblEdges,
                           self.tblCross] + list(self.tblEdges*numOfRows)
        self.lines = [headList, hrzBrdr]
        for num in range(numOfRows):
            self.lines.append([num, round(final.percLst[num]['lye'], 3),
                               round(final.percLst[num]['water'], 2)])

    def build_table(self):
        table = ''
        row = '{0:>{3}}{sep}{1:^{4}}{sep}{2:<{5}}'
        for line, sep in zip(self.lines, self.separators):
            table = table + '\n' + row.format(*line, *self.colmnW, sep=sep)
        table = '\n'.join(table.split('\n')[1:])  # removed 1st (blank) line
        return table


class OutPut:
    '''This object is the output dictionary ready to be boxed'''

    def __init__(self, final):
        self.outputDict = {}
        table = Table(final)
        self.outputDict['center1'] = 'VALUES\n'
        self.outputDict['left1'] = (
          '{f.oil} oil/{f.baseFull} saponification value:\n'
          '{f.sapV:.6f}\n\n'
          'Amount of {f.oil} oil:\n'
          '{f.oilAmnt:.3f} grams\n'
        ).format(f=final)
        self.outputDict['center2'] = (
          'Table for calculating a remaining-fat percentage\n'
          '(recommended about 5 - 8%)\n'
        )
        self.outputDict['center3'] = table.build_table()


class Box(Line_Characters):
    '''Construct a box around the input'''

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


def get_input(inputType, valueType, listOfItems=[]):
    prompt = getattr(Prompts(), valueType)
    if inputType == 'float':
        while True:
            value = input(prompt)
            try:
                return float(value)
                break
            except ValueError:
                print("That's not a number")
    elif inputType == 'str':
        while True:
            value = input(prompt).lower()
            if value in listOfItems:
                return value
                break
            else:
                print('{} not found in {} list'.format(value, valueType))


def showResults(final):
    ''' Prints out the results '''
    boxed = Box()
    outputs = OutPut(final)
    print(boxed.put_in_box(outputs.outputDict))


def main():
    '''Main Function'''
    oilList = list(SAP_Basics().__dict__.keys())
    baseList = list(Base_Ratios().__dict__.keys())
    oil = get_input('str', 'oil', oilList)
    oilAmnt = get_input('float', 'oilAmnt')
    base = get_input('str', 'base', baseList)
    final = Final_Values(oil, oilAmnt, base)
    showResults(final)


main()
