# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 09:34:03 2018

@author: hinson

The datetime module provides time objects that are similar to the Time objects
in this chapter, but they provide a rich set of methods and operators. Read the documentation at
http: // docs. python. org/ 3/ library/ datetime. html .
1. Use the datetime module to write a program that gets the current date and prints the day of
the week.
2. Write a program that takes a birthday as input and prints the user’s age and the number of
days, hours, minutes and seconds until their next birthday.
3. For two people born on different days, there is a day when one is twice as old as the other.
That’s their Double Day. Write a program that takes two birthdays and computes their Double
Day.
4. For a little more challenge, write the more general version that computes the day when one
person is n times older than the other
"""

import datetime

rules = {0: "Monday",
         1: "Tuesday",
         2: "Wednesday",
         3: "Thursday",
         4: "Friday",
         5: "Saturday",
         6: "Sunday"}


class Time(object):
    now = datetime.datetime.now()

    def __init__(self, year=1, month=1, day=1, hour=0, minute=0, second=0):
        self.date = datetime.datetime(year, month, day, hour, minute, second)

today = Time().now
birthday = Time(1953, 5, 24).date


def day_of_week():
    return "1) Today is %s" % rules[today.weekday()]


def birthday_stats(birthday):
    age = today.year - birthday.year
    if (birthday.month == today.month) and (birthday.day <= today.day):
        pass
    elif birthday.month < today.month:
        pass
    else:
        age -= 1

    birthday_ = Time(today.year, birthday.month, birthday.day).date
    till_birthday = str(birthday_ - today).split()

    if len(till_birthday) > 1:
        days = int(till_birthday[0])
        time = till_birthday[2].split(":")
    else:
        days = 365
        time = till_birthday[0].split(":")

    hours = time[0]
    mins = time[1]
    secs = time[2][:2]

    if (days < 0) and (days != 365):
        days = 365 + days
    elif (days == 365):
        days = 0
    else:
        days = abs(days)

    print ("2) You are %s years old; %sd:%sh:%sm:%ss until your next birthday."
    % (age, days, hours, mins, secs))

print (day_of_week())
birthday_stats(birthday)