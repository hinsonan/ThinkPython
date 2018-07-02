# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:26:13 2018

@author: hinson


Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy
these requirements. Solution: http: // thinkpython2. com/ code/ cartalk2. py .
"""

def print_pal_nums():
    for num in range(100000, 1000000):
        if str(num)[::-1] == str(num):
            print(num)
            
print_pal_nums()