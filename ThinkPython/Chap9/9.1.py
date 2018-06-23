# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:03:52 2018

@author: hinson

Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).
"""
def read_file():
    file = open('words.txt')
    for line in file:
        lineWithoutWhiteSpace = line.replace(" ", "").strip()
        if len(lineWithoutWhiteSpace) > 20:
            print(line)

read_file()


