# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:52:44 2018

@author: hinson

This exercise pertains to the so-called Birthday Paradox, which you can read about
at http: // en. wikipedia. org/ wiki/ Birthday_ paradox .
If there are 23 students in your class, what are the chances that two of you have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for
matches. Hint: you can generate random birthdays with the randint function in the random
module.
You can download my solution from http: // thinkpython2. com/ code/ birthday. py

"""
import random

def has_duplicates(listToCheck: list):
    sortedList = listToCheck
    sortedList.sort()
    for i in range(len(sortedList) - 1):
        if sortedList[i] == sortedList[i + 1]:
            return True
    return False

def birthday_duplicates():
    birthdays = []
    count = 0
    i = 0
    while i < 100:
        for items in range(23):
            birthdays.append(random.randint(1,365))

        if has_duplicates(birthdays):
                count += 1
        i +=1
    return count/i * 100

print(birthday_duplicates())
