#!/usr/bin/python

from scipy.misc import comb

k, m, n = 20, 20, 26 #Homo dom, hetero, homo rec

#Number of possible crossings times number of possible phenotypes (4, AA, Aa, Aa, aa)
offsprings = 4 * comb(k + m + n, 2)

#Number of dominant offsprings
# comb only for k*k and m*m
dominant_offsprings = 4*comb(k,2) + 4*k*m + 4*k*n + 3*comb(m,2) + 2*m*n

print dominant_offsprings/offsprings
