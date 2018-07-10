# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:38:56 2018

@author: hinson

Write a function called cumsum that takes a list of numbers and returns the cumulative
sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list
"""
numbers = [1, 2, 3]

def cumsum(listOfInts):
    total = 0
    cumsum = []
    for num in listOfInts:
       total += num
       cumsum.append(total)
    return cumsum

print(cumsum(numbers))

