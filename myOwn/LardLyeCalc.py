#!/usr/bin/python

# Set constants
#  soponificationValueLye = 0.1399
soponificationValueLard = 0.1387303
# soponificationValueLye = 0.138
solutionConstant = 0.3 # for 

# Ask for user input - how much lard by weight
lardValue = float(raw_input("\n\nHow much lard are you using? "))

# calculate lye 100, 99 98 97 96 95 94 93 92 91 and 90 percent
# (Amount of Fat) x (Saponification Value of the Fat) = (Amount of Lye)
lyeValue = []
for num in range(0,11):
    lyeValue.append((lardValue * soponificationValueLard) * ((100 - num) * .01))

# calculate lye/water at 100, 99 98 97 96 95 94 93 92 91 and 90 percent
# (Amount of Lye) / 0.3 = (Total Weight of Lye Water Solution)
lyeWaterValue = []
for num in range(0,11):
    lyeWaterValue.append((lyeValue[num] / solutionConstant))

# calculate water 100, 99 98 97 96 95 94 93 92 91 and 90 percent
# (Total Weight of Lye Water Solution) - (Amount of Lye) = (Amount of Water)
waterValue = []
for num in range(0,11):
    waterValue.append((lyeWaterValue[num] - lyeValue[num]))

# present results
print('''       Values by weight

Lard sValue:\t%f
Lard:\t\t%.2f


Table for calculating a remaining-fat percentage
(recommendted about 5%s):

percent\t|lye\t|water\t|lye and water
--------+-------+-------+-------------''' % (soponificationValueLard, lardValue, '%'))

# Creates table with remaining fat percentage, lye value, water value, and lye plus water value
for percent, lye, water, lyewater in zip(range(0,11), lyeValue, waterValue, lyeWaterValue):
    print("%d%s\t|%.2f\t|%.2f\t|%.2f" % (percent, '%', lye, water, lyewater))
    
print("\n\n")
