# Mendel's First Law
# Return probability that two randomly seleced mating organisms will produce an
# individual possessing a dominant allele (and thus displaying the dominant phenotype).
# 07/10/2015

import random

#k individuals are homozygous dominant for a factor, m are heterozygous,
#and n are homozygous recessive.
k = int(raw_input("Enter k: "))
m = int(raw_input("Enter m: "))
n = int(raw_input("Enter n: "))

dominant, hetero, recessive = k, m, n

total = dominant + hetero + recessive

r_r = ((recessive/total)*((recessive - 1))/(total - 1))
print r_r
h_h = ((hetero / total) * ((hetero - 1)) / (total - 1))
print h_h
h_r = (hetero / total) * ((recessive / (total - 1)) + (recessive / total) * (hetero / (total - 1)))
print h_r

recessive_total = r_r + h_h * 1/4 + h_r * 1/2
print str(1 - recessive_total)



