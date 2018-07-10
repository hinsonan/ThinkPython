# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:16:54 2018

@author: hinson

Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams
"""

def is_anagram(wordOne: str, wordTwo: str):
    wordOneList = list(wordOne.replace(" ", ""))
    wordTwoList = list(wordTwo.replace(" ", ""))
    wordOneList.sort()
    wordTwoList.sort()
    return ''.join(wordOneList) == ''.join(wordTwoList)

print(is_anagram('dog','cast'))

print(is_anagram('a decimal point','im a dot in place'))

    

