import os, sys
outfile = open("gene.bed", 'w')
for a in open(sys.argv[1], 'r') :
    if a[0] != "#" :
        if a.split("\t")[2] == "exon" :
            outfile.write(a.split("\t")[0]+"\t"+a.split("\t")[3]+"\t"+a.split("\t")[4]+"\t"+a.split("\t")[-1])
outfile.close()
