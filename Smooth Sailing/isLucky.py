# Author: Eric Oropezaelwood

"""
Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first 
half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.
"""

def isLucky(n):
    
    newArray = list(map(int, str(n))) 

    frontHalf = 0
    backHalf = 0

    for i in range(int(len(newArray)/2)):
        frontHalf += newArray[i]

    for i in range(int(len(newArray)/2), int(len(newArray))):
        backHalf += newArray[i]

    if frontHalf == backHalf:
        return 1

    return 0