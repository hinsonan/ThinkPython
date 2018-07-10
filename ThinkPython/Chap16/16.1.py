# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 08:36:47 2018

@author: hinson

Write a function called mul_time that takes a Time object and a number and returns
a new Time object that contains the product of the original Time and the number.
Then use mul_time to write a function that takes a Time object that represents the finishing time
in a race, and a number that represents the distance, and returns a Time object that represents the
average pace

"""


class Time:
    
    def __init__(self, hour = 10, minute = 51, second = 30):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        print ('%.2d hours %.2d minutes and %.2d seconds' % (self.hour, self.minute, self.second))
    
def get_seconds(time: Time):
    return ((3600*time.hour)+(60*time.minute)+(time.second))

def seconds_to_time(sec) -> Time:
    time = Time()
    time.hour=sec/3600
    sec=sec%3600
    time.minute=sec/60
    time.second=sec%60
    return time

def mul_time(time,n):
    secs=get_seconds(time)*n
    return seconds_to_time(int(round(secs)))
    
def pace(ftime, miles):
    return mul_time(ftime,1.0/miles)

def main():
    time = Time()
    time.__str__()
    time2 = mul_time(time, 3)
    time2.__str__()
    time3 = pace(time2, 4)
    time3.__str__()    
    
main()
    