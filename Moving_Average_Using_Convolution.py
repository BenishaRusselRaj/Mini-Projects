# -*- coding: utf-8 -*-
"""
Created on Fri May 16 14:51:06 2025

@author: IITM
"""
import numpy as np


#%%
def Moving_Average(inputArray, size, weight):
    x = inputArray
    
    y = np.array([weight] * size)
    
    return np.convolve(x, y)

#%%
windowSize = 3

valueWeight = 1/windowSize

x = np.array([5, 2, 3, 8, 1])

movingAvg = Moving_Average(x, windowSize, valueWeight)