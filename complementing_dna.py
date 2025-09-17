# -*- coding: utf-8 -*-

file = open(r"*\rosalind_revc (1).txt")

dna_string_data = file.read()

output_string = ''

for i in dna_string_data[::-1]:  
    if i=='A':
        output_string += 'T'
    elif i=='T':
        output_string += 'A'
    elif i=='C':
        output_string += 'G'
    elif i=='G':
        output_string += 'C'
    else:
        output_string += ''
        

print(output_string)
