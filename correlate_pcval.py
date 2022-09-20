import os,sys

gene_list = []
gene_dict = {}
gene_dict_corr = {}
for a in open("tpm.out", 'r') :
    if a.split("\t")[0] != "" :
        gene_list.append(a.split("\t")[0])
        gene_dict_corr[a.split("\t")[0]] = 0
gene_list = set(gene_list)

for a in open("tpm.out", 'r') :
    if a.split("\t")[0] != "" :
        br1p = float(a.split("\t")[-1].strip("\n"))
        br2p = float(a.split("\t")[2])
        br3p = float(a.split("\t")[4])
        br4p = float(a.split("\t")[3])
        br1s = float(a.split("\t")[1])
        br2s = float(a.split("\t")[5])
        br3s = float(a.split("\t")[-2])
        br4s = float(a.split("\t")[7])
        br1ps = float(a.split("\t")[-4])
        br2ps = float(a.split("\t")[-5])
        br3ps = float(a.split("\t")[6])
        br4ps = float(a.split("\t")[-3])
        gene_dict[a.split("\t")[0]] = [br1p, br2p, br3p, br4p, br1s, br2s, br3s, br4s, br1ps, br2ps, br3ps, br4ps] 

pcval = []
for a in open("pcval.txt", 'r') :
    if a.split("\t")[0] != '"PC1"' : 
        pcval.append(float(a.split("\t")[1]))

## reorder pcval 
pcval_corrected = [pcval[-1], pcval[2], pcval[4], pcval[3], pcval[1], pcval[5], pcval[-2], pcval[7], pcval[-4], pcval[-5], pcval[6], pcval[-3]]

print pcval_corrected

import scipy.stats as stats

output = open("gene_correlation_pc1.txt", 'w')
for gene in gene_list :
    output.write(gene+"\t"+str(stats.pearsonr(gene_dict[gene], pcval_corrected)[0])+"\n")
    print gene, stats.pearsonr(gene_dict[gene], pcval_corrected)[0]
output.close()

      


