# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:41:53 2018

@author: hinson
"""
def main():
    #this is not legal 42 - n
    
    #this is legal
    x = y = 1
    #you don't need a semicolon in python but it will compile and run
    #following the standards and conventions it is probaly best not to use semicolons
    print('this line ends in a semicolon');
    # the line below will not execute becuase of the period at the end of the statment
    print('this line ends in a period').

    #In math notation you can multiply x and y like this: xy. 
    #What happens if you try that in Python?
    x = 5
    y = 2
    
    print(xy) #this cuases an error becuase xy is not defined.
    #It thinks you are printing a variable called xy which does not exist
    
main()