# Author: Eric Oropezaelwood
#
"""
Given an array of integers, find the pair of adjacent elements that
has the largest product and return that product.
"""

def adjacentElementsProduct(inputArray):
    
    endAllBeAllArray = []
    # create a new array of products from input array
    for c in range(len(inputArray)-1):
        endAllBeAllArray.append(inputArray[c]*inputArray[c+1])
    
    answer = max(endAllBeAllArray)
    return answer