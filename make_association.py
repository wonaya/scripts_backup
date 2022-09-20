import os,sys

# gene \t association ; 
gene_list = []
gene_dict = {}
for a in open("mart_export_gene_go.txt" ,'r') :
    gene_list.append(a.split(",")[0])
    gene_dict[a.split(",")[0]] = []
gene_list = set(gene_list)

for a in open("mart_export_gene_go.txt" ,'r') :
    if len(a.split(",")[1].strip("\n")) > 1 :
        gene_dict[a.split(",")[0]].append(a.split(",")[1].strip("\n"))

outfile = open("Association_File.txt", 'w')
for gene in gene_list : 
    if len(gene_dict[gene]) > 0 :
        outfile.write(gene+"\t"+";".join(gene_dict[gene])+";\n")
outfile.close()

## get population
gene_pop = []
for a in open("tpm.out", 'r') :
    if a.split("\t")[0] != "" :
        gene_pop.append(a.split("\t")[0])
gene_pop = set(gene_pop)
outfile = open("pop.txt", 'w') 
for gene in gene_pop :
    outfile.write(gene+"\n")
outfile.close()

## get set
gene_set = []
for a in open("gene_correlation_pc1.txt" ,'r' ) :
    if float(a.split("\t")[1].strip("\n")) > 0.75 : 
        gene_set.append(a.split("\t")[0])
outfile = open("set.txt", 'w') 
for gene in gene_set :
    outfile.write(gene+"\n")
outfile.close()
