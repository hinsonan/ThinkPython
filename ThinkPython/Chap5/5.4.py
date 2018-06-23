# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:16:37 2018

@author: hinson
"""

"""
Exercise 5.4.
What is the output of the following program? Draw a stack diagram that shows the
state of the program when it prints the result.
    def recurse(n, s):
        if n == 0:
            print(s)
        else:
            recurse(n-1, n+s)
    recurse(3, 0)
1.  What would happen if you called this function like this:
    recurse(-1, 0) ?
2.  Write a docstring that explains everything someone would need to know in
    order to use this function (and nothing else).
"""

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

'''

recurse:
    n -> 3
    s -> 0
    
recurse:
    n -> 2
    s -> 3
recurse:
    n -> 1
    s -> 5
recurse:
    n -> 0
    s -> 6
    
'''


# recurse(-1, 0) will be infinite recursion.