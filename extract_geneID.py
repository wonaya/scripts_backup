import os,sys

genes = []
for a in open(sys.argv[1],'r') :
    
    if a[0] != "#" and a.split("\t")[2][-4:] == "gene" and a.split("\t")[-1].split(";")[0].strip("ID=gene:") not in genes :
        genes.append(a.split("\t")[-1].split(";")[0].strip("ID=gene:"))
        #print a.split("\t")[-1].split(";")[0].strip("ID=gene:")
    #print a.split("\t")[-1].split(";")[0]
    #if a.split("\t")[-1].split(";")[0].strip("ID=gene:")[0] != "Z" :
    #    print  a.split("\t")[-1].split(";")[0].strip("ID=gene:")
for gene in genes: 
    print gene
#for a in open(sys.argv[1],'r') :
#    print a.split("\t")[0]
