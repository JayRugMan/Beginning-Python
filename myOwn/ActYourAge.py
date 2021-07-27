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
    theAge={}
    # Converts the given birthday to datetime format
    b_dayDate = datetime.datetime.strptime(b_day, '%m/%d/%Y-%H:%M:%S')
    timeDifference = current_dt - b_dayDate
    
    # Calculates years as float and as interger - int goes into final dict
    years = ((timeDifference.total_seconds()) / (365.242*24*3600))
    theAge['years'] = int(years)
    
    # Calculates Months from the decimal remainder of 
    # difference between the year float and year interger
    months =(years - theAge['years']) * 12
    theAge['months'] = int(months)
    
    # Same as months, but for days
    days =(months - theAge['months']) * (365.242/12)
    theAge['days'] = int(days)
    
    # I think you get the point...
    hours = (days - theAge['days']) * 24
    theAge['hours'] = int(hours)
    
    # ... and on...
    minutes = (hours - theAge['hours']) * 60
    theAge['minutes'] = int(minutes)
    
    # ... to seconds.
    seconds = (minutes - theAge['minutes']) * 60
    theAge['seconds']  = int(seconds)
    
    return theAge


def main():
    '''
    The main event
    '''
    rightNow = datetime.datetime.now()
    birthday = get_birthday()
    age = calc_age(rightNow, birthday)
    finalStr = 'You are {years} years, ' + \
               '{months} months, ' + \
               '{days} days, ' + \
               '{hours} hours, ' + \
               '{minutes} minutes, ' + \
               'and {seconds} seconds old.'
    print(finalStr.format(**age))


main()
