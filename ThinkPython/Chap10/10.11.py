# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 12:48:06 2018

@author: hinson


Two words are a “reverse pair” if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list. Solution: http: // thinkpython2. com/ code/
reverse_ pair. py

"""

with open('../Chap9/words.txt') as fd:
    word_list = fd.read().splitlines()

word_dict = {word: None for word in word_list}

def find_rev_pairs(word_dict):
    for word in word_dict:
        if word[::-1] in word_dict:
            print (word, word[::-1])

find_rev_pairs(word_dict)