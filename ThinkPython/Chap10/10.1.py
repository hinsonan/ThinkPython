# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:13:14 2018

@author: hinson

Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists
"""
numbers =  [[1, 2], [3], [4, 5, 6]]
def nested_sum(listOfInts) -> int:
    total = 0
    for item in listOfInts:
        for nestedItem in item:
            total += nestedItem
    return total
    
    
print(nested_sum(numbers))
