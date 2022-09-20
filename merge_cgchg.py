# use python script.py methratio.txt 

import os,sys

outfile = open(sys.argv[2],'w')
for a in open(sys.argv[1], 'r') :
    if a.split("\t")[0] == "chr" :
        outfile.write(a)
    else :
        if a.split("\t")[3] == "CG" or a.split("\t")[3] == "CHG" :
            outfile.write("\t".join(a.split("\t")[:3]))
            outfile.write("\t")
            outfile.write("CG\t")
            outfile.write("\t".join(a.split("\t")[4:]))
outfile.close()

