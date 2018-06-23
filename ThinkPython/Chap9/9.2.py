# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:28:19 2018

@author: hinson

Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
it.
Modify your program from the previous section to print only the words that have no “e” and compute
the percentage of the words in the list that have no “e”.
"""

def has_no_e(word) -> bool:
     if word.find('e') == -1:
         return True
     else:
         return False
     

             
def read_file():
    file = open('words.txt')
    for line in file:
        if has_no_e(line.strip()):
            print(line)
            

read_file()
        
            