import os,sys

outfile = open("all_genes.txt", 'w')
gene_list = []
for a in open(sys.argv[1], 'r') :
    if a[0] != "#" :
        if a.split("\t")[2] == "gene" :
            gene_list.append(a.split("\t")[-1].split(";")[0].split(":")[1])
gene_list = set(gene_list)
for gene in gene_list :
    outfile.write(gene+"\n")
outfile.close()
