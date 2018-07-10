# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:57:03 2018

@author: hinson

Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None.
"""

numbers = [1,2,3,4,5,6,7,8,9]

def chop(listOfInts):
    del listOfInts[0]
    del listOfInts[len(listOfInts)-1]
    
print(chop(numbers))
