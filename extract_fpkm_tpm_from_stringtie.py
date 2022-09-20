import sys, os

fpkm_f = open(sys.argv[1].strip(".out")+"_fpkm.out", 'w')
tpm_f  = open(sys.argv[1].strip(".out")+"_tpm.out" , 'w')
for a in open(sys.argv[1], 'r') : 
    if a[0] != "#" and len(a.split("\t")[-1].split(";")) > 7 :
        gene = a.split("\t")[-1].split(";")[3].split(" ")[2].strip('"gene:')
        fpkm = a.split("\t")[-1].split(";")[5].split(" ")[2].strip('"')
        tpm =  a.split("\t")[-1].split(";")[6].split(" ")[2].strip('"')
        fpkm_f.write(gene+"\t"+fpkm+"\n")
        tpm_f.write(gene+"\t"+tpm+"\n")
fpkm_f.close()
tpm_f.close()
