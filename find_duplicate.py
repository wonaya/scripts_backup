import os,sys

genes = []

for a in open(sys.argv[1],'r') :
    if a.split("\t")[0] in genes : 
        print a
    genes.append(a.split("\t")[0])
