# -*- coding: utf-8 -*-

f = open(r"*\rosalind_dna (2).txt")

dna_data = f.read()

for i in 'ACGT':
    val_count = dna_data.count(i)

    print (val_count)
