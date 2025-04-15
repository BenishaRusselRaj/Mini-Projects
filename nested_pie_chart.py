# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 17:26:11 2025

@author: IITM
"""
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
vals = np.array([[60, 32], [37, 40], [29, 10]])

size = 0.3
# colorseq = plt.colormaps()   #['tab20c']

# outer_color = [colorseq[i] for i in [0, 4, 8]] colors = inner_color,
# inner_color = [colorseq[i] for i in [1, 2, 3, 5, 6, 9, 10]]  colors = outer_color,

ax.pie(vals.sum(axis = 1), radius = 1, autopct = "%1.1f%%",
       wedgeprops = dict(width = size, edgecolor = 'w'))

ax.pie(vals.flatten(), radius = 1 - size, autopct = "%1.1f%%",
       wedgeprops = dict(width = size, edgecolor = 'w'))

ax.set(aspect = 'equal', title = 'Nested Pie Chart')

plt.show()