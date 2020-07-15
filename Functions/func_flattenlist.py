# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:36:08 2020

@author: lucys
"""

# Problem 9
# 15/15 points (graded)
# Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    result = []
    for elt in aList:
        if type(elt) != list:
            result.append(elt)
        else:
            result.extend(flatten(elt))
    return result