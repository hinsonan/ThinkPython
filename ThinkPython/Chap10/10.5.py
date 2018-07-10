# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:04:40 2018

@author: hinson

Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise

"""
numbers = [2,4,6,1,8,33,9]

def is_sorted(listOfInts):
    for i in range(len(listOfInts) -1):
        if listOfInts[i] > listOfInts[i + 1]:
            return False
    return True

print( is_sorted(numbers))