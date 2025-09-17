# -*- coding: utf-8 -*-

f = open(r"*\rosalind_rna.txt")

dna_data = f.read()

rna_data = dna_data.replace('T', 'U')


print(rna_data)
