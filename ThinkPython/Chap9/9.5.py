# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:16:47 2018

@author: hinson

Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once.
"""

def uses_all(word, string):
    for letter in string:
        if letter not in word:
            return False
    return True

print(uses_all('test', 'ae'))

