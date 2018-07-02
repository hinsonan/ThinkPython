# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:44:53 2018

@author: hinson

Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. 

"""

def uses_only(word: str, string: str) -> bool:
    for letter in word:
        if letter not in string:
            return False
    return True

print(uses_only('test', 'te'))
    

