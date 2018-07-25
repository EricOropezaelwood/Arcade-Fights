# Author: Eric Oropezaelwood

"""
Given an array of strings, return another array containing
all of its longest string.
"""

def allLongestStrings(inputArray):
    
    # find longest length string in given array
    big = max(len(s) for s in inputArray)
    # find all string of size 'big'
    result = [s for s in inputArray if len(s) == big]
    
    return result
