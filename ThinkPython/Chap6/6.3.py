# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:55:26 2018

@author: hinson

Write a function called is_palindrome that takes a string argument and returns True if it
is a palindrome and False otherwise. Remember that you can use the built-in function len
to check the length of a string.

"""

import palindrome

def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif palindrome.first(word) == palindrome.last(word):

        if len(palindrome.middle(word)) == 1:
            return True
        else:
            return is_palindrome(palindrome.middle(word))

    else:
        return False


print(is_palindrome('level'))
print(is_palindrome('car'))
