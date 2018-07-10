# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:28:57 2018

@author: hinson

Memoize the Ackermann function from Exercise 6.2 and see if memoization
makes it possible to evaluate the function with bigger arguments.
"""

known_m = {}
known_n = {}
def ack(m,n):
    if m in known_m and n in known_n:
            return 

    
    if m == 0:
        return n+1
        
    if n == 0:
        return ack(m-1,1)

    return ack(m-1, ack(m,n-1))


print(ack(3, 4))