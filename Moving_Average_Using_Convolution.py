# -*- coding: utf-8 -*-

import numpy as np
import sys

#%%
def Moving_Average(inputArray, size, weight):
    x = inputArray
    
    y = np.array([weight] * size)
    
    return np.convolve(x, y)

#%%
windowSize = input("Enter the window size:")

try:
    valueWeight = 1/windowSize
except:
    print ("Enter a valid window size!")
    sys.exit(1)

x = np.array([5, 2, 3, 8, 1])

movingAvg = Moving_Average(x, windowSize, valueWeight)
