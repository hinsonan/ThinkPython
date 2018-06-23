# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 08:52:24 2018

@author: hinson
The following functions are all intended to check whether a string contains any
lowercase letters, but at least some of them are wrong. For each function, describe what the function
actually does (assuming that the parameter is a string).


"""
#This function will terminate too soon. This function only checks the first letter of a string and returns the appropriate 
def any_lowercase1(s):
    for c in s:
            if c.islower():
                return True
            else:
                return False
            
#This will always return true becuase it is checking the string 'c' and not the actual word you passed in
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
        
#this function only test if the last letter is upper or lowercase
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
    
#This function behaves as it should. flag is set to false and gets reassigned to True if the letter is lowercase.
#Once reassigned to True you can not set it back to false
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
    
#this function test if the whole entire word is lowercase.
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True