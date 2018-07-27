# Author: Eric Oropezaelwood
"""
Some people are standing in a row in a park. There 
are trees between them which cannot be moved. Your 
task is to rearrange the people by their heights in 
a non-descending order without moving the trees. 
People can be very tall!
"""

def sortByHeight(a):
    
    trees = sorted([c for c in a if c > 0])
    for x,c in enumerate(a):
        if c == -1:
            trees.insert(x,c)
    return trees