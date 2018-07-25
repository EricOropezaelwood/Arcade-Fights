# Author: Eric Oropezaelwood
#
"""
Given a polygon n, find the area given in terms of 1,4,7. These numbers
represent how many blocks the shape is on all sides.
"""

def shapeArea(n):
    
    result = (n*n) + ((n-1)*(n-1))
    return result