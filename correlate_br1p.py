import os,sys

from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
from scipy.stats import pearsonr

genelist = []
genedict = {}
for a in open("/scratch/02114/wonaya/NCSU/Zm_B73_RNA-seq_0-1mm_Steady_State_primary_seminal_2021.05.24/stringtie_exmode/merge_htseq_tpm_withoutbr4.txt", 'r') :
    if a[0] != "G" :
        genelist.append(a.split("\t")[0])
        genedict[a.split("\t")[0]] = float(a.split("\t")[2])

genedict2 = {}
for a in open("/scratch/02114/wonaya/NCSU/Zm_B73_RNA-seq_0-1mm_Steady_State_primary_seminal_2021.05.24/stringtie_exmode/merge_sumtpm_withoutbr4.txt", 'r') :
    if a[0] != "G" :
        genedict2[a.split("\t")[0]] = float(a.split("\t")[1])

val1 = []
val2 = []

for gene in genelist :
    val1.append(genedict[gene])
    val2.append(genedict2[gene])

print max(val1), max(val2)

corr, _ = pearsonr(val1, val2)
print('Pearsons correlation: %.3f' % corr)

pyplot.scatter(val1, val2)
pyplot.xlabel("htseq")
pyplot.ylabel("stringtie")
pyplot.show()
