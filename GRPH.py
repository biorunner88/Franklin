#!/usr/bin/python

from Bio import SeqIO

#Functions

def function(lista, n):
	over_graph = []
	for x1, y1 in lista:
		for x2, y2 in lista:
			if x1 != x2 and y1.endswith(y2[:n]):
				over_graph.append((x1,x2))
	
	return over_graph
	
#Script
with open("rosalind_grph.txt", "r") as file:
	
	file = SeqIO.parse( file , "fasta")
	
	lista = []

	for i in file:
		lista.append((i.id, str(i.seq)))
		

final = function(lista,3)
				
for i in final:
	print i[0], i[1]
			
