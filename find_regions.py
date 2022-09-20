import os,sys

outfile = open("syntenic_genes_b73.txt", 'w')
filelist = []
for line in open("SF_50.5_B73v4.36_Sbv3.1_W22v2-nodups.txt", 'r') :
    for a in line.split("autogo=1") :
        filelist.append(a)
gene_list=[]
gene_dict = {}
outfile.write("B73\tSorghum\tW22\n")
for a in filelist :     
    if a.split("\t")[0][1:3].strip("\n") =="Zm" and a.split("\t")[2] != "no detected annotated syntelog" and a.split("\t")[3] != "nonsyntologous region" and a.split("\t")[2] != "nonsyntologous region" and a.split("\t")[3] != "no detected annotated syntelog" :
        outfile.write(a.split("\t")[0][1:]+"\t")
        outfile.write(a.split("\t")[2].split(".")[1])
        outfile.write(a.split("\t")[3]+"\n")
        # b73
        #gene_list.append(a.split("\t")[0][1:])
        #gene_dict[a.split("\t")[0][1:]] = a.split("\t")[0][1:]
        # sorghum gene = b73 gene
        #gene_dict[a.split("\t")[2].split(".")[1]] = a.split("\t")[0][1:]
        # w22 gene 
        gene_dict[a.split("\t")[3].strip("\n")] = a.split("\t")[0][1:]
        gene_list.append(a.split("\t")[3].strip("\n"))
        #print gene_dict ; sys.exit()
outfile.close()
#print gene_dict ; sys.exit()
### gene
gene_list = set(gene_list) ; print len(gene_list)
file1 = open(sys.argv[1], 'r')
lines1 = file1.readlines()
outfile = open("file1.txt",'w')
for line in lines1[1:] :
    if line.split("\t")[0] in gene_list :
    #print line.split("\t")[0]
    #if line.split("\t")[0][:8] == "gene:SOR" and line.split("\t")[0].split("SORBI_3")[1] in gene_list :
        #outfile.write(line.split("\t")[0]+"\t"+line.split("\t")[-4]+"\n")       
        #outfile.write(gene_dict[line.split("\t")[0].split("SORBI_3")[1]]+"\t"+line.split("\t")[-4]+"\n")
        outfile.write(gene_dict[line.split("\t")[0]]+"\t"+line.split("\t")[-4]+"\n")
outfile.close()   

file1 = open(sys.argv[2], 'r')
lines1 = file1.readlines()
outfile = open("file2.txt",'w')
for line in lines1[1:] :
    if line.split("\t")[0] in gene_list :
    #if line.split("\t")[0][:8] == "gene:SOR" and line.split("\t")[0].split("SORBI_3")[1] in gene_list :
        #outfile.write(gene_dict[line.split("\t")[0].split("SORBI_3")[1]]+"\t"+line.split("\t")[-4]+"\n")
        #outfile.write(line.split("\t")[0]+"\t"+line.split("\t")[-4]+"\n")
        outfile.write(gene_dict[line.split("\t")[0]]+"\t"+line.split("\t")[-4]+"\n")
        #outfile.write(gene_dict[line.split("\t")[0]]+"\t"+line.split("\t")[-4]+"\n")
outfile.close()

file1 = open(sys.argv[3], 'r')
lines1 = file1.readlines()
outfile = open("file3.txt",'w')
for line in lines1[1:] :
    #if line.split("\t")[0][:8] == "gene:SOR" and line.split("\t")[0].split("SORBI_3")[1] in gene_list :
    if line.split("\t")[0] in gene_list :
        #outfile.write(gene_dict[line.split("\t")[0].split("SORBI_3")[1]]+"\t"+line.split("\t")[-4]+"\n")
        #outfile.write(line.split("\t")[0]+"\t"+line.split("\t")[-4]+"\n")
        outfile.write(gene_dict[line.split("\t")[0]]+"\t"+line.split("\t")[-4]+"\n")
        #outfile.write(gene_dict[line.split("\t")[0]]+"\t"+line.split("\t")[-4]+"\n")
outfile.close()

outfile = open("merged.txt", 'w')
gene_list = []
for a in open("file1.txt", 'r') :
    gene_list.append(a.split("\t")[0])

for gene in gene_list :
    list = []
    for a in open("file1.txt",'r') :
        if a.split("\t")[0] == gene :
            #outfile.write(gene+"\t"+a.split("\t")[1].strip("\n"))
            list.append(gene)
            list.append(a.split("\t")[1].strip("\n"))
    for a in open("file2.txt", 'r'):
        if a.split("\t")[0] == gene :
            #outfile.write("\t"+a.split("\t")[1].strip("\n"))
            list.append(a.split("\t")[1].strip("\n"))
    for a in open("file3.txt", 'r'):
        if a.split("\t")[0] == gene :
            #outfile.write("\t"+a.split("\t")[1])
            list.append(a.split("\t")[1].strip("\n"))
    if len(list) == 4 :
        outfile.write("\t".join(list)+"\n")
outfile.close()

