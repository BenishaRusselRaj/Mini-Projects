# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 17:36:15 2025

@author: CBEEV
"""

f = open(r"C:\Users\CBEEV\Downloads\rosalind_rna.txt")

dna_data = f.read()

rna_data = dna_data.replace('T', 'U')

print(rna_data)