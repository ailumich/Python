# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:15:09 2020

@author: lucys
"""

import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    bucket = ['r','r','r','g','g','g']
    result = 0
    for trial in range(numTrials):
        copy = bucket.copy()
        temp = []
        for i in range(3):
            x = random.choice(copy)
            temp.append(x)
            copy.remove(x)
        if ['r','r','r'] == temp or ['g','g','g'] == temp:
            result += 1
     
    return result/numTrials