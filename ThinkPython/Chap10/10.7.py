# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:36:39 2018

@author: hinson
. Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list
"""
listOfChar = ['c', 'b', 'a', 'c']

def has_duplicates(listToCheck: list):
    sortedList = listToCheck
    sortedList.sort()
    for i in range(len(sortedList) - 1):
        if sortedList[i] == sortedList[i + 1]:
            return True
    return False


print(has_duplicates(listOfChar))