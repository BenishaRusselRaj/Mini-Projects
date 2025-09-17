# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:31:29 2025

@author: CBEEV
"""

f = open(r"C:\Users\CBEEV\Downloads\rosalind_dna (2).txt")

dna_data = f.read()

for i in 'ACGT':
    val_count = dna_data.count(i)
    print (val_count)