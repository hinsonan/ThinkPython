# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:00:49 2018

@author: hinson
"""

#Write a function named check_fermat that takes four parameters—a, b, c and n—and
#checks to see if Fermat’s theorem holds. If n is greater than 2 and
#a
#n + b
#n = c
#n
#the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
#print, “No, that doesn’t work.”
#2. Write a function that prompts the user to input values for a, b, c and n, converts them to
#integers, and uses check_fermat to check whether they violate Fermat’s theorem

def check_fermat(a,b,c,n):
    if(((a**n + b**n) == c**n) and n > 2 ):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('“No, that doesn’t work')
        
def main():
    a = int(input('input integer for a\n'))
    b = int(input('input integer for b\n'))
    c = int(input('input integer for c\n'))
    n = int(input('input integer for n\n'))
        
    check_fermat(a,b,c,n)
    
main()
   


            