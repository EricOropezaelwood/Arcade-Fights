# Author: Eric Oropezaelwood

"""
Given two strings, find the number of common characters between them.
"""

def commonCharacterCount(s1, s2):
    
    similar = [min(s1.count(i), s2.count(i)) for i in set(s1)]
    
    return sum(similar)