#!/usr/bin/python3
# lyeCalc.py

from jaymatting import Box, Line_Characters
import lyeStuff


class Table(Line_Characters.Tables):
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
            table += '\n' + row.format(*line, *self.colmnW, sep=sep)
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


def get_input(inputType, valueType, listOfItems=[]):
    prompt = getattr(lyeStuff.Prompts(), valueType)
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
    boxed = Box.Box()
    outputs = OutPut(final)
    print(boxed.put_in_box(outputs.outputDict))


def main():
    '''Main Function'''
    oilList = list(lyeStuff.SAP_Basics().__dict__.keys())
    baseList = list(lyeStuff.Base_Ratios().__dict__.keys())
    oil = get_input('str', 'oil', oilList)
    oilAmnt = get_input('float', 'oilAmnt')
    base = get_input('str', 'base', baseList)
    final = lyeStuff.Final_Values(oil, oilAmnt, base)
    showResults(final)


main()
