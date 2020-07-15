# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:51:56 2020

@author: lucys
"""
import statistics
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    listlen = []
    if len(L) == 0:
        return float('NaN')
    else:
        for i in L:
            temp = len(i)
            listlen.append(temp)
    return statistics.pstdev(listlen)