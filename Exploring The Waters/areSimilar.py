# Eric Oropezaelwood

"""
Two arrays are called similar if one can be obtained from another by 
swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.
"""

def areSimilar(a, b):
    
    # the arrays are exactly similar
    if a == b:
        return True
    
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            if a == b:
                return True
            a[j] = a[i]
            a[i] = temp
            
    return False