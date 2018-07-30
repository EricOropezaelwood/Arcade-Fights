# Eric Oropezaelwood

"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
"""

def addBorder(picture):
    
    lengthOfString = len(picture[0]) + 2
    
    return ['*' * lengthOfString] + [x.center(lengthOfString,'*') for x in picture] + ['*' * lengthOfString]