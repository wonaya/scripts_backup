##
import os,sys

#log2fpkm
gene_list = []
for a in open(sys.argv[1],'r') :
    gene_list.append(a.split("\t")[0])
for a in open(sys.argv[2],'r') :
    gene_list.append(a.split("\t")[0])
for a in open(sys.argv[3],'r') :
    gene_list.append(a.split("\t")[0])
for a in open(sys.argv[4],'r') :
    gene_list.append(a.split("\t")[0])
for a in open(sys.argv[5],'r') :
    gene_list.append(a.split("\t")[0])
for a in open(sys.argv[6],'r') :
    gene_list.append(a.split("\t")[0])

gene_list = set(gene_list)
#gene_list.sort()
print "gene count", len(gene_list)

## filter protein coding 
pc_gene_list = []
for a in open(sys.argv[7], 'r') :
    if a[0] != "#" : 
       if a.split("\t")[-1].split(";")[-2].strip("") == ' gene_biotype "protein_coding"':
           pc_gene_list.append(a.split("\t")[-1].split(";")[0].split('"')[1]) 
pc_gene_list = set(pc_gene_list)
gene_list = pc_gene_list

import numpy as math

outfile = open("merged_all_log2_higherthan1andlowerthan10.txt" ,'w')
outfile.write("Gene\tEU BR1\tEU BR2\tEU BR3\tSS BR1\tSS BR2\tSS BR3\n")
for gene in gene_list :
    val = [gene,0,0,0,0,0,0]
    for a in open(sys.argv[1],'r') :
        if a.split("\t")[0] == gene and a.split("\t")[9].strip("\n") != "FPKM" :
            val[1] += math.log2(float(a.split("\t")[9].strip("\n"))+1)
            break
    for a in open(sys.argv[2],'r') :
        if a.split("\t")[0] == gene and a.split("\t")[9].strip("\n") != "FPKM" :
            val[2] += math.log2(float(a.split("\t")[9].strip("\n"))+1)
            break
    for a in open(sys.argv[3],'r') :
        if a.split("\t")[0] == gene and a.split("\t")[9].strip("\n") != "FPKM" :
            val[3] += math.log2(float(a.split("\t")[9].strip("\n"))+1)
            break
    for a in open(sys.argv[4],'r') :
        if a.split("\t")[0] == gene and a.split("\t")[9].strip("\n") != "FPKM" :
            val[4] += math.log2(float(a.split("\t")[9].strip("\n"))+1)
            break
    for a in open(sys.argv[5],'r') :
        if a.split("\t")[0] == gene and a.split("\t")[9].strip("\n") != "FPKM" :
            val[5] += math.log2(float(a.split("\t")[9].strip("\n"))+1)
            break
    for a in open(sys.argv[6],'r') :
        if a.split("\t")[0] == gene and a.split("\t")[9].strip("\n") != "FPKM" :
            val[6] += math.log2(float(a.split("\t")[9].strip("\n"))+1)
            break
    #if val != [gene,0,0,0,0,0,0] :
    #if 0 is not in val :
    if any(t < 1 for t in val) and any(t > 10 for t in val) :
        continue
    else :
        outfile.write("\t".join(map(str,val))+"\n")
outfile.close()
