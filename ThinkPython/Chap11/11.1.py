# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 14:59:10 2018

@author: hinson

Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.
"""


file = open('words.txt')

def create_word_dict():
    word_dict = dict()
    for line in file:
        word = line.strip()
        word_dict[word] = word
    return word_dict

print(create_word_dict())