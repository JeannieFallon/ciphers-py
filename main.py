# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:40:16 2019

@author: jfall
"""

import cipher

# Basic CLI cipher application

### FUNCTIONS ###

def getCaesar(plnStr):
    # method stub
    ciphStr = cipher.getSingleShift(plnStr)
    return ciphStr

def getVigenere(plnStr):
    # method stub
    ciphStr = cipher.getMultiShift(plnStr)
    return ciphStr

### MAIN PROGRAM ###
    
plnStr = "This is an input plain string."

print("Plain string: " + plnStr)
print("Single-shift cipher string: " + getCaesar(plnStr))
print("Multi-shift cipher string: " + getVigenere(plnStr))