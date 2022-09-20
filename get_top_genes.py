import os,sys

outfile2 = open("all_genes.txt", 'w') 
outfile = open("DESeq2_top_genes.txt", 'w')
for a in open("ReadCountMatrix_pvalsort_count_DESeq2.txt" ,'r') :
    if a[0:2] != '"b' :
        if a.split("\t")[-1].strip("\n") !=  "NA" :
            outfile2.write(a.split("\t")[0].strip('"')+"\n")
            if float(a.split("\t")[-1].strip("\n")) <= 0.001 and float(a.split("\t")[-1].strip("\n")) >= -0.001 : 
                print a.split("\t")[0].strip('"'), a.split("\t")[1], float(a.split("\t")[-1].strip("\n"))
                outfile.write(a.split("\t")[0].strip('"')+"\n")
outfile.close()
outfile2.close()
