#!/usr/bin/env python
import argparse
import pandas as pd
import os, sys

gene_dict = {}
for a in open("Aligned.BR1Primary.gtf.featurecounts.bedGraph", 'r') :
    gene_dict[a.split("\t")[-1].strip("\n")] = "\t".join(a.split("\t")[:3])

outfile = open("lengths.txt", 'w')
outfile.write("Geneid\tlength\n")
for a in open("Aligned.BR1Primary.gtf.featurecounts.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        outfile.write(a.split("\t")[0]+"\t"+str(int(a.split("\t")[5])-1)+"\n")
outfile.close()

parser = argparse.ArgumentParser(description='convert counts to tpm values')
parser.add_argument('-i', '--infile', help='counts values csv file', required =True)
#parser.add_argument('-l', '--length', help='list of gene name and length', required =True)
parser.add_argument('-o', '--outfile', help='converted values csv file', required =True)

args = parser.parse_args()
length = "lengths.txt"
infile = args.infile
out = args.outfile


df_counts = pd.read_csv(infile,sep=',')
df_length = pd.read_csv(length,sep='\t')

df_col = pd.merge(df_length, df_counts, on='Geneid')
df_col ['length'] = df_col['length'].div(1000)
# divide read counts by length of each gene in kilobase (reads per kilobase
df_col.update(df_col.iloc[:,2:].div(df_col['length'], axis="index"))

df_permil= df_col.iloc[:,2:].sum(axis=0)
#scaling factor permil
df_permil = df_permil/1000000

df_col.update(df_col.iloc[:,2:]/df_permil)
df_col.to_csv(out,sep='\t',index=False)
#os.system("rm -Rf lengths.txt")

sys.exit()
## write individual bedGraph
bamlist = []
for a in open(out, 'r') :
    if a[0] == "G" :
        for b in a.split("\t")[2:] : 
            bamlist.append(b.strip("\n"))

for bam in bamlist :
    index = bamlist.index(bam)+2
    outfile = open(bam.strip(".bam")+"_tpm.bedGraph", 'w') 
    for a in open(out, 'r') :
        if a[0] != "#" and a[0] != "G" :
            outfile.write("\t".join(gene_dict[a.split("\t")[0]].split("\t"))+"\t")
            outfile.write(a.split("\t")[index].strip("\n")+"\t"+a.split("\t")[0]+"\n") 
    outfile.close()

    os.system("/work2/02114/wonaya/software/bedtools2/bin/sortBed -i "+bam.strip(".bam")+"_tpm.bedGraph > "+bam.strip(".bam")+"_tpm.bedGraph.sorted")
    os.system("mv "+bam.strip(".bam")+"_tpm.bedGraph.sorted "+bam.strip(".bam")+"_tpm.bedGraph")
