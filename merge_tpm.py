import os,sys

geneid = []
for a in open("BR1Primary_Stringtie_ExMode.out", 'r') :
    if a[0] != "#" and a.split("\t")[2] == 'transcript' :
        geneid.append(a.split("\t")[-1].split(";")[0].split("gene:")[1].strip('"'))
geneid = set(geneid)
genedict = {}
for gene in geneid :
    genedict[gene] = []

#br1p = []
for a in open("BR1Primary_Stringtie_ExMode.out", 'r') :
    if a[0] != "#" and a.split("\t")[2] == 'transcript' :
        #geneid.append(a.split("\t")[-1].split(";")[0].split('gene:')[1].strip('"'))
        #transcriptid.append(a.split("\t")[-1].split(";")[1].split('transcript_id "transcript:')[1].strip('"'))
        tpm = a.split("\t")[-1].split(";")[-2].split("TPM ")[1].strip('"') 
        #br1p.append(tpm)
        gene = a.split("\t")[-1].split(";")[0].split("gene:")[1].strip('"')
        genedict[gene].append(float(tpm))
#br2p = []
for a in open("BR2Primary_Stringtie_ExMode.out", 'r') :
    if a[0] != "#" and a.split("\t")[2] == 'transcript' :
        tpm = a.split("\t")[-1].split(";")[-2].split("TPM ")[1].strip('"') 
        gene = a.split("\t")[-1].split(";")[0].split("gene:")[1].strip('"')
        genedict[gene].append(float(tpm))
        #br2p.append(tpm)
br3p = []
for a in open("BR3Primary_Stringtie_ExMode.out", 'r') :
    if a[0] != "#" and a.split("\t")[2] == 'transcript':
        tpm = a.split("\t")[-1].split(";")[-2].split("TPM ")[1].strip('"') 
        br3p.append(tpm)
#br4p = []
#for a in open("Aligned.BR4Primary.gtf.featurecounts.txt", 'r') :
#    if a[0] != "#" :
#        br4p.append(a.split("\t")[-1].strip("\n"))
br1s = []
for a in open("BR1Seminal_Stringtie_ExMode.out", 'r') :
     if a[0] != "#" and a.split("\t")[2] == 'transcript':
        tpm = a.split("\t")[-1].split(";")[-2].split("TPM ")[1].strip('"')
        br1s.append(tpm)
br2s = []
for a in open("BR2Seminal_Stringtie_ExMode.out", 'r') :
    if a[0] != "#" and a.split("\t")[2] == 'transcript' :
        tpm = a.split("\t")[-1].split(";")[-2].split("TPM ")[1].strip('"')
        br2s.append(tpm)
br3s = []
for a in open("BR3Seminal_Stringtie_ExMode.out", 'r') :
    if a[0] != "#" and a.split("\t")[2] == 'transcript' :
        tpm = a.split("\t")[-1].split(";")[-2].split("TPM ")[1].strip('"')
        br3s.append(tpm)
#br4s = []
#for a in open("Aligned.BR4Seminal.gtf.featurecounts.txt", 'r') :
#    if a[0] != "#" :
#        br4s.append(a.split("\t")[-1].strip("\n"))
br1ps = []
for a in open("BR1Primary_seminal_Stringtie_ExMode.out" ,'r') :
    if a[0] != "#" and a.split("\t")[2] == 'transcript' :
        tpm = a.split("\t")[-1].split(";")[-2].split("TPM ")[1].strip('"')
        br1ps.append(tpm)
br2ps = []
for a in open("BR2Primary_seminal_Stringtie_ExMode.out" ,'r') :
    if a[0] != "#" and a.split("\t")[2] == 'transcript' :
        tpm = a.split("\t")[-1].split(";")[-2].split("TPM ")[1].strip('"')
        br2ps.append(tpm)
br3ps = []
for a in open("BR3Primary_seminal_Stringtie_ExMode.out" ,'r') :
    if a[0] != "#" and a.split("\t")[2] == 'transcript' :
        tpm = a.split("\t")[-1].split(";")[-2].split("TPM ")[1].strip('"')
        br3ps.append(tpm)
#br4ps = []
#for a in open("Aligned.BR4Primary_seminal.gtf.featurecounts.txt" ,'r') :
#    if a[0] != "#" :
#        br4ps.append(a.split("\t")[-1].strip("\n"))

outfile = open("merge_featurecount_withoutbr4.txt", 'w') 
outfile.write("GeneID\tBR1P\tBR2P\tBR3P\tBR1S\tBR2S\tBR3S\tBR1PS\tBR2PS\tBR3PS\n")
for x in range(0, len(br1p)) :
    #outfile.write(geneid[x]+","+br1p[x]+","+br2p[x]+","+br3p[x]+","+br4p[x]+","+br1s[x]+","+br2s[x]+","+br3s[x]+","+br4s[x]+","+br1ps[x]+","+br2ps[x]+","+br3ps[x]+","+br4ps[x]+"\n")
    outfile.write(transcriptid[x]+"\t"+br1p[x]+"\t"+br2p[x]+"\t"+br3p[x]+"\t"+br1s[x]+"\t"+br2s[x]+"\t"+br3s[x]+"\t"+br1ps[x]+"\t"+br2ps[x]+"\t"+br3ps[x]+"\n")
outfile.close()

