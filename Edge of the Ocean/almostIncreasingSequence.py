# Author: Eric Oropezaelwood

"""
Given a sequence of integers as an array, determine whether 
it is possible to obtain a strictly increasing sequence by 
removing no more than one element from the array.
"""

def almostIncreasingSequence(sequence):
    
    removed = False
    last = previous = min(sequence) - 1
    for i in sequence:
        if i <= last:
            if removed:
                return False
            else:
                removed = True
            if i <= previous:
                previous = last
            elif i >= previous:
                previous = last = i
        else:
            previous, last = last, i
            
    return True