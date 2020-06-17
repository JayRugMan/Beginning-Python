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


class Base_Ratios:
    '''Na base ratio based on Na molecular wieght devided by K molecular weight
    or 39.997 g/mol divided by 56.106 g/mol'''

    def __init__(self):
        self.naoh = 1402.755
        self.koh = 1000


class Prompts:
    '''List of prompts to be used when getting input'''

    def __init__(self):
        self.oilList = ' '.join(list(SAP_Basics().__dict__.keys()))
        self.oil = 'Type of oil ({}): '.format(self.oilList)
        self.oilAmnt = 'How many grams: '
        self.base = 'Type of base (NaOH KOH): '


class Final_Values():
    '''Class to keep the final values for output and calculate output.
    This calculates lye amounts for oil provided. The SAP value is the
    average amount of potassium Hydroxide (KOH) in micrograms needed
    to saponify the specified oil.'''

    def __init__(self, oil, amount, base):
        # solution contant or solCon is to achieve lye/water ratio of 35%:65%
        self.solCon = 0.35
        self.oil = oil
        self.oilAmnt = amount
        if base == 'naoh':
            self.baseFull = 'sodium hydroxide'
        elif base == 'koh':
            self.baseFull = 'potassium hydroxide'
        else:
            raise Exception('Sorry, you entered an unknown base!')
        self.sapV = getattr(SAP_Basics(), oil)/getattr(Base_Ratios(), base)
        # Calcluate amount of Lye based on amount of oil(fat) and Sap value
        # (Amount of Fat) x (Saponification Value of the Fat) = (Amount of Lye)
        self.lyeAmnt = amount * self.sapV
        self.waterAmnt = self.lyeAmnt*(1/self.solCon - 1)
        # calculate lye 100, 99 98 97 96 95 94 93 92 91 and 90 percent
        self.percLst = []
        for num in range(11):
            self.percLst.append({'lye': self.lyeAmnt*((100-num)*0.01)})
            self.percLst[num]['water'] = int(self.waterAmnt*((100-num)*0.01))


def get_input(type):
    prompt = getattr(Prompts(), type)
    output = input(prompt)
    try:
        return float(output)
    except ValueError:
        return output.lower()


def screen_input(valueType, inputType, listOfItems=[]):
    if valueType == 'number':
        while True:
            value = get_input(inputType)
            try:
                float(value)
                break
            except ValueError:
                print("That's not a number")
    elif valueType == 'list':
        while True:
            value = get_input(inputType)
            if value in listOfItems:
                break
            else:
                print('{} not found in list'.format(value))
    return value


def showResults(final):
    ''' Prints out the results '''
    print('''\n       Values by weight

{oil} oil/{baseFull} Saponification Value:
{sapV:.6f}

Amount of {oil} oil:
{oilAmnt:.3f} grams

Table for calculating a remaining-fat percentage
(recommended about 5 - 8%):

|percent  |lye (g)\t|water (ml)\t
+---------+-------------+-----------'''.format(**final.__dict__))
    # Creates table with remaining fat percentage,
    # lye value, water value, and lye plus water value
    for num in range(11):
        print('|{0}\t  |{lye:.3f}\t|{water}'.format(num, **final.percLst[num]))
    print('\n')


def main():
    '''Main Function'''
    oil = screen_input('list', 'oil', list(SAP_Basics().__dict__.keys()))
    oilAmnt = screen_input('number', 'oilAmnt')
    base = screen_input('list', 'base', list(Base_Ratios().__dict__.keys()))
    final = Final_Values(oil, oilAmnt, base)
    showResults(final)


main()
