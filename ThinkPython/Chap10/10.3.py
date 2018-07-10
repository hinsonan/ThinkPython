# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:42:53 2018

@author: hinson

Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements.

"""

numbers = [1,2,3,4,5]

def middle(listOfInts):
    middleList = listOfInts
    del middleList[0]
    lengthOfList = len(middleList)
    del middleList[lengthOfList - 1]
    return middleList


print(middle(numbers))

