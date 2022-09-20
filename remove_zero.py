import os,sys

outfile = open(sys.argv[1]+"_nonzero.bedgraph", 'w')

for a in open(sys.argv[1], 'r') :
    if a.split("\t")[-1].strip("\n") != '0' :
        outfile.write(a)
outfile.close()
