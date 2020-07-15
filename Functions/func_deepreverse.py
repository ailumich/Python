# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:02:37 2020

@author: lucys
"""

# Problem 6
# 15/15 points (graded)
# Implement a function that meets the specifications below.

# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    result = []
    for i in L:
        result.append(i[::-1])
    L[:] = result[::-1]
    

