# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 12:12:05 2018

@author: hinson
Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?
"""

import time

f = open('../Chap9/words.txt')

def build_list1():
    word_list = []
    for line in f:
        word = line.strip()
        word_list.append(word)
    return word_list

def build_list2():
    word_list = []
    for line in f:
        word = line.strip()
        word_list += [word]
        
print(build_list1())
print(build_list2())