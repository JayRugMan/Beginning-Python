#!/usr/bin/python3

# Print out a date, given year, month, and day as numbers
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# A list with one endeing for each number from 1 to 31
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st']

year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

# Remember to subtract 1 from the month and day to get a correct index
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

# print(month_name + ' ' + ordinal + ', ' + year)
final = '{} {}, {}'
print(final.format(month_name, ordinal, year))
