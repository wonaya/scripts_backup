import os,sys

posfc = open("positive_logfc.txt", 'w')
negfc = open("negative_logfc.txt", 'w')

outfile = open("deseq2_output_sig.txt", 'w')
outfile.write("\tbase\n")
for a in open("deseq2_output.txt",'r') :
    if a[0] != "b" :
        if a.split("\t")[2] != "NA" and a.split("\t")[-1].strip("\n") != "NA" :
            if float(a.split("\t")[-1].strip("\n")) < 0.05 : 
                if float(a.split("\t")[2]) > 0.58 :  
                    outfile.write(a)
                    posfc.write(a.split("\t")[0]+"\n")
                elif float(a.split("\t")[2]) < -0.58 :
                    outfile.write(a)
                    negfc.write(a.split("\t")[0]+"\n")
outfile.close()
posfc.close()
negfc.close()

