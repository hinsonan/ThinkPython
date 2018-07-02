# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:32:06 2018

@author: hinson

Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
"""

def avoids(word: str, letters: str) -> bool:
    for character in letters:
        if letters in word:
            return False    
    return True 

print(avoids('test', 's'))
        