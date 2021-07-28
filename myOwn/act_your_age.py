#!/usr/bin/python3

#####
#
#  modeled and imporved upon https://gist.github.com/shahri23/1804a3acb7ffb58a1ec8f1eda304af1a
#
#####

import datetime


def get_birthday():
    '''
    Asks for birthday input
    '''
    bday = input('When were you born (mm/dd/yyyy-hh:mm:ss)? ')
    return bday


def calc_age(current_dt, b_day):
    '''
    Takes birthday and current time to calculate age
    '''
    the_age={}
    # Converts the given birthday to datetime format
    b_daydate = datetime.datetime.strptime(b_day, '%m/%d/%Y-%H:%M:%S')
    time_difference = current_dt - b_daydate
    # Calculates years as float and as interger - int goes into final dict
    years = ((time_difference.total_seconds()) / (365.2425*24*3600))
    the_age['years'] = int(years)
    # Calculates Months from the decimal remainder of
    # difference between the year float and year interger
    months =(years - the_age['years']) * 12
    the_age['months'] = int(months)
    # Same as months, but for days
    days =(months - the_age['months']) * (365.242/12)
    the_age['days'] = int(days)
    # I think you get the point...
    hours = (days - the_age['days']) * 24
    the_age['hours'] = int(hours)
    # ... and on...
    minutes = (hours - the_age['hours']) * 60
    the_age['minutes'] = int(minutes)
    # ... to seconds.
    seconds = (minutes - the_age['minutes']) * 60
    the_age['seconds']  = int(seconds)
    return the_age


def main():
    '''
    The main event
    '''
    right_now = datetime.datetime.now()
    birthday = get_birthday()
    age = calc_age(right_now, birthday)
    final_str = 'You are {years} years, ' + \
               '{months} months, ' + \
               '{days} days, ' + \
               '{hours} hours, ' + \
               '{minutes} minutes, ' + \
               'and {seconds} seconds old.'
    print(final_str.format(**age))


main()
