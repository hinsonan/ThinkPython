# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:42:35 2018

@author: hinson


Write a definition for a class named Circle with attributes center and radius,
where center is a Point object and radius is a number.
Instantiate a Circle object that represents a circle with its center at (150, 100) and radius 75.
Write a function named point_in_circle that takes a Circle and a Point and returns True if the
Point lies in or on the boundary of the circle.
Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if
the Rectangle lies entirely in or on the boundary of the circle.
Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns
True if any of the corners of the Rectangle fall inside the circle. Or as a more challenging version,
return True if any part of the Rectangle falls inside the circle.

"""
import math
import copy

class Rectangle:
    
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner
        

class Circle:
    
    def __init__(self, center, radius = 0):
        self.center = center
        self.radius = radius
    
class Point:
   
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


def point_in_circle(Circle: Circle, Point: Point):
    distance = math.sqrt(((Point.x - Circle.center.x)**2) + ((Point.y - Circle.center.y)**2))
    if Circle.center.x == Point.x or Circle.center.y == Point.y:
        return True
    elif distance <= Circle.radius:
        return True
    else:
        return False
    
def rect_in_circle(circ: Circle, rect: Rectangle):
    point = copy.copy(rect.corner)
    if not point_in_circle(circ, point):
        return False
    
    point.x += rect.width
    if not point_in_circle(circ, point):
        return False

    point.y -= rect.height
    if not point_in_circle(circ, point):
        return False

    point.x -= rect.width
    if not point_in_circle(circ, point):
        return False
    
    return True
    
def rect_circle_overlap(rect: Rectangle, circ: Circle):
    point = copy.copy(rect.corner)
    if point_in_circle(circ, point):
        return True

    point.x += rect.width
    if point_in_circle(circ, point):
        return True

    point.y -= rect.height
    if point_in_circle(circ, point):
        return True

    point.x -= rect.width
    if point_in_circle(circ, point):
        return True

    return False
    
            
    
