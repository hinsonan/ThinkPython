# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 10:18:37 2018

@author: hinson

Write a function called most_frequent that takes a string and prints the letters
in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages
"""

def make_dict(word: str) -> dict:
    charDict = {}
    for letter in word:
        charDict[letter] = 1 + charDict.get(letter, 0)
    return charDict



def most_frequent(word: str):
    letters = [letter.lower() for letter in word if letter.isalpha()]   
    letterDict = make_dict(letters)
    frequentLetters = []
    for key in letterDict:
        frequentLetters.append((letterDict[key], key))
    frequentLetters.sort(reverse = True)
    for count, letter in frequentLetters:
        print(letter, count)
        

most_frequent('big dog')
