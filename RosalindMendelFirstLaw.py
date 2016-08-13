# Mendel's First Law
# Return probability that two randomly seleced mating organisms will produce an
# individual possessing a dominant allele (and thus displaying the dominant phenotype).
# 07/10/2015

import random

#k individuals are homozygous dominant for a factor, m are heterozygous,
#and n are homozygous recessive.

dominant = int(raw_input("Enter k: "))
hetero = int(raw_input("Enter m: "))
recessive = int(raw_input("Enter n: "))


print(dominant, hetero, recessive)

total = dominant + hetero + recessive

r_r = (recessive/total)* ((recessive - 1)/(total - 1))
h_h = (hetero / total) * ((hetero - 1) / (total - 1))
h_r = (hetero / total) * (recessive / (total - 1)) + (recessive / total) * (hetero / (total - 1))

recessive_total = r_r + (h_h * 1/4) + (h_r * 1/2)
print(recessive_total)



