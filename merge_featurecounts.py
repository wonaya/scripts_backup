import os,sys

geneid = []
br1p = []
for a in open("Aligned.BR1Primary.gtf.featurecounts.txt", 'r') :
    if a[0] != "#" :
        geneid.append(a.split("\t")[0])
        br1p.append(a.split("\t")[-1].strip("\n"))
br2p = []
for a in open("Aligned.BR2Primary.gtf.featurecounts.txt", 'r') :
    if a[0] != "#" :
        br2p.append(a.split("\t")[-1].strip("\n"))
br3p = []
for a in open("Aligned.BR3Primary.gtf.featurecounts.txt", 'r') :
    if a[0] != "#" :
        br3p.append(a.split("\t")[-1].strip("\n"))
#br4p = []
#for a in open("Aligned.BR4Primary.gtf.featurecounts.txt", 'r') :
#    if a[0] != "#" :
#        br4p.append(a.split("\t")[-1].strip("\n"))
br1s = []
for a in open("Aligned.BR1Seminal.gtf.featurecounts.txt", 'r') :
    if a[0] != "#" :
        br1s.append(a.split("\t")[-1].strip("\n"))
br2s = []
for a in open("Aligned.BR2Seminal.gtf.featurecounts.txt", 'r') :
    if a[0] != "#" :
        br2s.append(a.split("\t")[-1].strip("\n"))
br3s = []
for a in open("Aligned.BR3Seminal.gtf.featurecounts.txt", 'r') :
    if a[0] != "#" :
        br3s.append(a.split("\t")[-1].strip("\n"))
#br4s = []
#for a in open("Aligned.BR4Seminal.gtf.featurecounts.txt", 'r') :
#    if a[0] != "#" :
#        br4s.append(a.split("\t")[-1].strip("\n"))
br1ps = []
for a in open("Aligned.BR1Primary_seminal.gtf.featurecounts.txt" ,'r') :
    if a[0] != "#" :
        br1ps.append(a.split("\t")[-1].strip("\n"))
br2ps = []
for a in open("Aligned.BR2Primary_seminal.gtf.featurecounts.txt" ,'r') :
    if a[0] != "#" :
        br2ps.append(a.split("\t")[-1].strip("\n"))
br3ps = []
for a in open("Aligned.BR3Primary_seminal.gtf.featurecounts.txt" ,'r') :
    if a[0] != "#" :
        br3ps.append(a.split("\t")[-1].strip("\n"))
#br4ps = []
#for a in open("Aligned.BR4Primary_seminal.gtf.featurecounts.txt" ,'r') :
#    if a[0] != "#" :
#        br4ps.append(a.split("\t")[-1].strip("\n"))

outfile = open("merge_featurecount_withoutbr4.txt", 'w') 
for x in range(0, len(br1p)) :
    #outfile.write(geneid[x]+","+br1p[x]+","+br2p[x]+","+br3p[x]+","+br4p[x]+","+br1s[x]+","+br2s[x]+","+br3s[x]+","+br4s[x]+","+br1ps[x]+","+br2ps[x]+","+br3ps[x]+","+br4ps[x]+"\n")
    outfile.write(geneid[x]+","+br1p[x]+","+br2p[x]+","+br3p[x]+","+br1s[x]+","+br2s[x]+","+br3s[x]+","+br1ps[x]+","+br2ps[x]+","+br3ps[x]+"\n")
outfile.close()

