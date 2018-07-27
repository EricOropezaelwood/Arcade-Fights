# Author: Eric Oropezaelwood
"""
You have a string s that consists of English letters, 
punctuation marks, whitespace characters, and brackets. 
It is guaranteed that the parentheses in s form a regular 
bracket sequence.

Your task is to reverse the strings contained in each pair 
of matching parentheses, starting from the innermost pair. 
The results string should not contain any parentheses.
"""

def reverseParentheses(s):
    
    for i in range(len(s)):
        if s[i] == "(":
            beginning = i
        if s[i] == ")":
            ending = i
            return reverseParentheses(s[:beginning] + s[beginning+1:ending][::-1] + s[ending+1:])
    return s