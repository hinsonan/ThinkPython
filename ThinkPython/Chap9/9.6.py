# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:35:20 2018

@author: hinson

Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok).
 How many abecedarian words are there?
"""
def is_abecedarion(word):
    return word == ''.join(sorted(word))

def num_of_abecedarion_words():
    count = 0
    file = open('words.txt')
    for line in file:
        word = line.strip()
        if is_abecedarion(word):
            count += 1
            
    print('There are', count, 'abecedarian words.')
    
num_of_abecedarion_words()


