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
    '''Na base ratio based on Na molecular wieght devided by
    K molecular weight or 39.997 g/mol divided by 56.106 g/mol'''

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
