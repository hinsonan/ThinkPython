# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:25:51 2018

@author: hinson
"""

def is_triangle(sideOne, sideTwo, sideThree):
    if((sideOne > (sideTwo + sideThree)) or (sideTwo > (sideOne + sideThree)) or 
       (sideThree > (sideOne + sideOne))):
        print('No')
    else:
        print('Yes')
        
def main():
    sideOne = int(input('input integer for side one\n'))
    sideTwo = int(input('input integer for side two\n'))
    sideThree = int(input('input integer for side three\n'))
   
        
    is_triangle(sideOne, sideTwo, sideThree)
    
main()        