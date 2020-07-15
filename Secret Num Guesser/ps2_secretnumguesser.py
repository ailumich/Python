# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:03:02 2020

@author: lucys
"""

low = 0
high = 100
ans = (low + high)/2
print ("Please think of a number between 0 and 100!")
print("Is your secret number "+str(int(ans))+"?")
x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. Enter: ")

while x != "c":
    if x == "h":
        high = ans
    elif x == "l":
        low = ans
    elif x != "c":
        print("Sorry I did not understand your input")
    ans = (low + high)/2
    print("Is your secret number "+str(int(ans))+"?")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. Enter: ")
print("Game Over. Your secret number was: "+str(int(ans)))
