import os,sys

listdir = []
geneid = []
genedict = {}
br1p = []
for a in open("BR1_EU_nascent_S2_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        geneid.append(a.split("\t")[0])
        genedict[a.split("\t")[0]] = [0]*14
        genedict[a.split("\t")[0]][0] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR2_EU_nascent_merge_rRNA_free_aligned_consensusrmAligned.sort_no45s.featurecounts.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][1] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR3_EU_nascent_S4_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][2] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR4_EU_nascent_S12_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][3] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR5_EU_nascent_S17_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][4] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR1_EU_contol_S1_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][5] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR2_EU_contol_S9_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][6] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR3_EU_contol_S3_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][7] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR4_EU_contol_S11_rRNA_free_aligned_consensusrmAligned.sort_no45s.featurecounts.txt",'r'):
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][8] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR5_EU_contol_S13_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][9] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR1_Primary_and_seminal_S5_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt",'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][10] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR2_Primary_and_seminal_S8_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt",'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][11] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR3_Primary_and_seminal_S16_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt",'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][12] += int(a.split("\t")[-1].strip("\n"))
for a in open("BR4_Primary_and_seminal_S20_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt",'r') :
    if a[0] != "#" and a[0] != "G" :
        genedict[a.split("\t")[0]][13] += int(a.split("\t")[-1].strip("\n"))

outfile = open("merge_featurecount_eun_euc_pns.txt", 'w')
outfile.write("GeneID\tEUN-BR1\tEUN-BR2\tEUN-BR3\tEUN-BR4\tEUN-BR5\tEUC-BR1\tEUC-BR2\tEUC-BR3\tEUC-BR4\tEUC-BR5\tPS-BR1\tPS-BR2\tPS-BR3\tPS-BR4\n")
for gene in genedict.keys() :
    outfile.write(gene+"\t"+"\t".join(map(str,genedict[gene]))+"\n")
outfile.close()

## normalize by lowest
order = []
for a in open("merge_featurecount_eun_euc_pns.txt", 'r') :
    if a[0] == "G" :
        for b in a.split("\t")[1:] :
            order.append(b.strip("\n"))
    break 
sum_list = []
for x in range(1,15) :
    sum = 0
    for a in open("merge_featurecount_eun_euc_pns.txt", 'r') :
        if a[0] != "G" :
            sum += int(a.split("\t")[x].strip("\n"))
    sum_list.append(sum)
factor_list = []
min = min(sum_list)
for a in sum_list :
    factor = float(a)/float(min)
    factor_list.append(factor)
outfile = open("merge_featurecount_eun_euc_pns_norm.txt", 'w') 
for a in open("merge_featurecount_eun_euc_pns.txt", 'r') : 
    if a[0] == "G" :
        outfile.write(a)
    else :
        index = 0
        outfile.write(a.split("\t")[0])
        for b in a.split("\t")[1:] :
            outfile.write("\t")
            outfile.write(str(float(b.strip("\n"))/float(factor_list[index])))
            index += 1
        outfile.write("\n")
outfile.close()
##norm to TPM
## (readcount)/genelength(in Kb) = RPK
## scaling factor: sum RPK in sample / 1,000,000
## Divide RPK by scaling factor = TPM
## import gene length 
gene_dict = {}
for a in open("BR1_EU_nascent_S2_L004_rRNA_free_aligned.consensusaligned.STARAligned.sort_no45s.featurecounts.txt", 'r') :
    if a[0] != "G" and a[0] != "#" :
        gene_dict[a.split("\t")[0]] = int(a.split("\t")[-2])
outfile = open("merge_featurecount_RPK.txt", 'w')
for a in open("merge_featurecount_eun_euc_pns.txt", 'r') :
    if a[0] == "G" :
        outfile.write(a)
    else :
        index = 0
        outfile.write(a.split("\t")[0])
        for b in a.split("\t")[1:] :
            outfile.write("\t")
            gene1k = float(gene_dict[a.split("\t")[0]])/1000
            RPK = float(b.strip("\n"))/gene1k
            outfile.write(str(RPK))
            index += 1
        outfile.write("\n")
outfile.close()
rpk_sum_list = []
for x in range(1,15) :
    rpk_sum = 0
    for a in open("merge_featurecount_RPK.txt", 'r') :
        if a[0] != "G" :
            rpk_sum += float(a.split("\t")[x].strip("\n"))
    rpk_sum_list.append(rpk_sum)
rpk_factor_list = []
for a in rpk_sum_list :
    factor = float(a)/1000000
    rpk_factor_list.append(factor)
#print(rpk_factor_list)
outfile = open("merge_featurecount_TPM.txt", 'w')
for a in open("merge_featurecount_RPK.txt", 'r') :
    if a[0] == "G" :
        outfile.write(a)
    else :
        index = 0
        outfile.write(a.split("\t")[0])
        for b in a.split("\t")[1:] :
            outfile.write("\t")
            outfile.write(str(float(b.strip("\n"))/float(rpk_factor_list[index])))
            index += 1
        outfile.write("\n")
outfile.close()

#check total
sum_list = []
for x in range(1,10) :
    sum = 0
    for a in open("merge_featurecount_TPM.txt", 'r') :
        if a[0] != "G" :
            sum += float(a.split("\t")[x].strip("\n"))
    sum_list.append(sum)
print(sum_list)
