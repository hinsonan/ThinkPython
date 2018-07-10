# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:15:56 2018

@author: hinson

def binomial_coeff(n, k):
Compute the binomial coefficient "n choose k".
n: number of trials
k: number of successes
returns: int
if k == 0:
return 1
if n == 0:
return 0
res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
return res
Rewrite the body of the function using nested conditional expressions
"""

def binomial_coeff(n,k):
    if k == 0 : return 1
    if n == 0: return 0

    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    return res
    