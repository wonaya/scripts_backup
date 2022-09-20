import os,sys
import numpy as np
import math
list_2 = os.listdir(".")

fpkm_l = []
tpm_l  = []
for val in  list_2 :
    if len(val.split("_")) > 2 :
        if val.split("_")[-1] == "fpkm.out"   :
            fpkm_l.append(val)
        elif val.split("_")[-1] == "tpm.out"  : 
            tpm_l.append(val)
    
#print fpkm_l, tpm_l

## concatenate values 

## make dict
tpm_d = {}
tpm_d_log = {}
fpkm_d = {}
fpkm_d_log = {}
id_l = []
gene_list = []
for x in tpm_l :  
    id = x.split("_Stringtie")[0]
    if id not in id_l :
        id_l.append(id)
    for line in open(x, 'r') :
        gene_list.append(line.split("\t")[0])
print len(gene_list)
gene_list = set(gene_list)
print len(gene_list)
for gene in gene_list :
    tpm_d[gene] = [0]*len(tpm_l)
    fpkm_d[gene] = [0]*len(fpkm_l)
    tpm_d_log[gene] = [0]*len(tpm_l)
    fpkm_d_log[gene] = [0]*len(fpkm_l)

index = 0
for x in tpm_l : 
    print x
    for line in open(x, 'r') :
        tpm_d[line.split("\t")[0]][index] += float(line.split("\t")[1].strip("\n"))
        if float(line.split("\t")[1].strip("\n")) > 0 :
            tpm_d_log[line.split("\t")[0]][index] += np.log2(float(line.split("\t")[1].strip("\n")))
        else :
            tpm_d_log[line.split("\t")[0]][index] += 0
    index += 1

index = 0
for x in fpkm_l : 
    print x
    for line in open(x, 'r') :
        fpkm_d[line.split("\t")[0]][index] += float(line.split("\t")[1].strip("\n"))
        if float(line.split("\t")[1].strip("\n")) > 0 :
            fpkm_d_log[line.split("\t")[0]][index] += np.log2(float(line.split("\t")[1].strip("\n")))
        else :
            fpkm_d_log[line.split("\t")[0]][index] += 0
    index += 1

## write into file
tpm_out = open("tpm.out", 'w')
tpm_out.write("\t")
tpm_out.write("\t".join(tpm_l))
tpm_out.write("\n")
for gene in gene_list :
    tpm_out.write(gene+"\t"+"\t".join(np.array(tpm_d[gene],str))+"\n")
tpm_out.close()

## tpm log
tpm_out = open("tpm_log2.out", 'w')
tpm_out.write("\t")
tpm_out.write("\t".join(tpm_l))
tpm_out.write("\n")
for gene in gene_list :
    tpm_out.write(gene+"\t"+"\t".join(np.array(tpm_d_log[gene],str))+"\n")
tpm_out.close()

fpkm_out = open("fpkm.out", 'w')
fpkm_out.write("\t")
fpkm_out.write("\t".join(fpkm_l))
fpkm_out.write("\n")
for gene in gene_list :
    fpkm_out.write(gene+"\t"+"\t".join(np.array(fpkm_d[gene],str))+"\n")
fpkm_out.close()

##fpkm log
fpkm_out = open("fpkm_log2.out", 'w')
fpkm_out.write("\t")
fpkm_out.write("\t".join(fpkm_l))
fpkm_out.write("\n")
for gene in gene_list :
    fpkm_out.write(gene+"\t"+"\t".join(np.array(fpkm_d_log[gene],str))+"\n")
fpkm_out.close()
