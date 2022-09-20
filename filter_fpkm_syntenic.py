import os,sys

genes = []
outfile = open(sys.argv[3], 'w')
for a in open(sys.argv[2],'r') :
    # for b73 filter genes [0], sorghum [1], w22 [2]
    genes.append(a.split("\t")[0].strip("\n"))

genes = set(genes)

for b in open(sys.argv[1], 'r') :
    if b.split("\t")[0] in genes and b.split("\t")[-3] != "0" :
        outfile.write(b)
outfile.close()
