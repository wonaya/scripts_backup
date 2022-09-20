import os,sys

genelist = []
for a in open("merge_tpm_withoutbr4.txt", 'r') :
    if a.split("\t")[0] != "geneID" :
        genelist.append(a.split("\t")[0].split("_")[0])
genelist = list(dict.fromkeys(genelist))
genelist.sort()

gene_dict = {}
for gene in genelist :
    gene_dict[gene] = [[],[],[],[],[],[],[],[],[]]

for a in open("merge_tpm_withoutbr4.txt", 'r') :
    if a.split("\t")[0] != "geneID" :
        #print gene_dict[a.split("\t")[0].split("_")[0]] ; sys.exit()
        gene_dict[a.split("\t")[0].split("_")[0]][0].append(float(a.split("\t")[1]))
        #print a.split("\t")[0].split("_")[0], float(a.split("\t")[1]) ; sys.exit()
        gene_dict[a.split("\t")[0].split("_")[0]][1].append(float(a.split("\t")[2]))
        gene_dict[a.split("\t")[0].split("_")[0]][2].append(float(a.split("\t")[3]))
        gene_dict[a.split("\t")[0].split("_")[0]][3].append(float(a.split("\t")[4]))
        gene_dict[a.split("\t")[0].split("_")[0]][4].append(float(a.split("\t")[5]))
        gene_dict[a.split("\t")[0].split("_")[0]][5].append(float(a.split("\t")[6]))
        gene_dict[a.split("\t")[0].split("_")[0]][6].append(float(a.split("\t")[7]))
        gene_dict[a.split("\t")[0].split("_")[0]][7].append(float(a.split("\t")[8]))
        gene_dict[a.split("\t")[0].split("_")[0]][8].append(float(a.split("\t")[9].strip("\n")))
        #print gene_dict[a.split("\t")[0].split("_")[0]] ; sys.exit()

outfile = open("merge_sumtpm_withoutbr4.txt", 'w') 
outfile.write("geneID\tBR1P\tBR2P\tBR3P\tBR1S\tBR2S\tBR3S\tBR1PS\tBR2PS\tBR3PS\n")
for gene in genelist :
    #print gene, sum(gene_dict[gene][0])
    outfile.write(gene+"\t"+str(sum(gene_dict[gene][0]))+"\t"+str(sum(gene_dict[gene][1]))+"\t")
    outfile.write(str(sum(gene_dict[gene][2]))+"\t"+str(sum(gene_dict[gene][3]))+"\t")
    outfile.write(str(sum(gene_dict[gene][4]))+"\t"+str(sum(gene_dict[gene][5]))+"\t")
    outfile.write(str(sum(gene_dict[gene][6]))+"\t"+str(sum(gene_dict[gene][7]))+"\t")
    outfile.write(str(sum(gene_dict[gene][8]))+"\n")
outfile.close()
