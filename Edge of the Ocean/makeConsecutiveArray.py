# Author: Eric Oropezaelwood
# From Code Fights
"""
Ratiorg got statues of different sizes as a present from CodeMaster 
for his birthday, each statue having an non-negative integer size. 
Since he likes to make things perfect, he wants to arrange them from 
smallest to largest so that each statue will be bigger than the 
previous one exactly by 1. He may need some additional statues to be 
able to accomplish that. Help him figure out the minimum number of 
additional statues needed.
"""

def makeArrayConsecutive2(statues):
    
    counter = 0
    # sort the given array smallest to biggest
    statues.sort()
    
    for i in range(len(statues)-1):
        if statues[i]+1 != statues[i+1]:
            counter += (statues[i+1] - statues[i]) -1
        else:
            continue
            
    return counter
