# Author: Eric Oropezaelwood
#
"""
Given a string, check if it is a palindrome.
"""

def checkPalindrome(inputString):
    # start from the end up until the start of the string
    if inputString[::-1] == inputString:
        return True
    else:
        return False