#!/usr/bin/python3

# Set constants
#  source https://www.fromnaturewithlove.com/resources/sapon.asp
# Basic SAP value per oil in key
sapB = {
    'pig': 193,
    'lard': 194.60420115,
    'coconut': 258,
    'castor': 181
}
# Na base ratio based on Na molecular wieght devided by K molecular weight
# or 39.997 g/mol divided by 56.106 g/mol
NAvsKRatio = {"Na": 1402.755, "K": 1000}
oilList = ', '.join(list(sapB.keys()))
prompts = {
    'oil': 'Type of oil ({}): '.format(oilList),
    'oil amount': 'How many grams of {oil} oil: ',
    'base': 'Type of base (Na, K): '
}
responses = {}
calcdAmnts = {}
solCon = 0.35  # Solution Constant, for calculating water/lye ratio


def getInput(prompt):
    ''' This gets input base on desigated prompt and returns value.'''
    value = input(prompt)
    return value


def buildResponse():
    ''' This builds the response dictionary.'''
    for key in prompts.keys():
        if key == "oil amount":
            responses[key] = float(getInput(prompts[key].format(**responses)))
        else:
            responses[key] = getInput(prompts[key])


def calcLye():
    '''This calculates lye amounts for oil provided.
    The SAP value is the average amount of potassium
    in micrograms needed to saponify the specified oil.'''
    kSapVal = sapB[responses['oil']]
    baseRatio = NAvsKRatio[responses['base']]
    calcdAmnts['sapVal'] = kSapVal / baseRatio
    # Calcluate amount of Lye based on amount of oil(fat) and Sap value
    oil_amount = responses['oil amount']
    sapValue = calcdAmnts['sapVal']
    # (Amount of Fat) x (Saponification Value of the Fat) = (Amount of Lye)
    calcdAmnts['lye amount'] = round(oil_amount * sapValue, 3)
    # calculate lye 100, 99 98 97 96 95 94 93 92 91 and 90 percent
    for num in range(11):
        calcdAmnts[num] = {'lye': calcdAmnts['lye amount']*((100-num)*.01)}
        calcdAmnts[num]['water'] = int(calcdAmnts[num]['lye']*(1/solCon - 1))
        calcdAmnts[num]['lye'] = round(calcdAmnts[num]['lye'], 3)


def showResults():
    ''' Prints out the results '''
    output = {'oil': responses['oil'],
              'oil amount': responses['oil amount'],
              'sap value': calcdAmnts['sapVal']}
    print('''\n       Values by weight

{oil} oil Saponification Value:\t{sap value:.6f}
Amount of {oil} oil:\t\t{oil amount:.2f}

Table for calculating a remaining-fat percentage
(recommended about 5 - 8%):

|percent  |lye (g)\t|water (ml)\t
+---------+-------------+-----------'''.format(**output,))
# Creates table with remaining fat percentage,
# lye value, water value, and lye plus water value
    for num in range(11):
        print('|{0}\t  |{lye:.3f}\t|{water}'.format(num, **calcdAmnts[num]))
    print('\n')


def main():
    buildResponse()
    calcLye()
    showResults()


main()
