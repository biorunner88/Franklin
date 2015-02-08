#!/usr/bin/python

from Bio import SeqIO
from Bio.SeqUtils import GC

file = open("rosalind_gc.txt", "r")

GC_amount = 0
for sequence in SeqIO.parse(file,"fasta"):
	if GC(sequence.seq) > GC_amount:
		sequence_id = sequence.id
		GC_amount = GC(sequence.seq)

file.close()

print sequence_id
print GC_amount
