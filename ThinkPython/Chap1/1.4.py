# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:33:03 2018

@author: hinson
"""

def main():
    seconds = (43 * 60) + 30
    miles = 10/1.61
    milesPerHour = 60 / ((seconds/miles)/60)
    #g argument in the format removes insignificant zeros and rounds to 2nd decimal place
    print('The Runners pace for this race is {0:.3g}mph' .format(milesPerHour))
    
main()