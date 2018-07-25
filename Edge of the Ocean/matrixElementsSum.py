# Author: Eric Oropezaelwood

"""
After they became famous, the CodeBots all decided to move to 
a new building and live together. The building is represented 
by a rectangular matrix of rooms. Each cell in the matrix 
contains an integer that represents the price of the room. 
Some rooms are free (their cost is 0), but that's probably 
because they are haunted, so all the bots are afraid of them. 
That is why any room that is free or is located anywhere below 
a free room in the same column is not considered suitable for 
the bots to live in.

Help the bots calculate the total price of all the rooms that 
are suitable for them.
"""

def matrixElementsSum(matrix):
    
    total = 0;
    
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix)):
            if (matrix[j][i] == 0):
                break
            else:
                total += matrix[j][i]

    else:
        return total