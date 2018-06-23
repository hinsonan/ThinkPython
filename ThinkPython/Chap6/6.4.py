# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:03:25 2018

@author: hinson

A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case
"""

def is_power(a, b):
    if a == b:
        return True
    elif a%b == 0:
        return is_power(a/b, b)
    else:
        return False

print(is_power(7, 7))
print(is_power(1, 3))
