import os,sys

name = sys.argv[1].split(".bam")[0]
print name
os.system("/work/02114/wonaya/stampede2/software/samtools-1.9/samtools flagstat "+sys.argv[1])
os.system("/work/02114/wonaya/stampede2/software/samtools-1.9/samtools view -b -f 0X43 "+sys.argv[1]+" > "+name+"_0x43.bam")
os.system("/work/02114/wonaya/stampede2/software/samtools-1.9/samtools view -b -f 0X83 "+sys.argv[1]+" > "+name+"_0x83.bam")
os.system("/work/02114/wonaya/stampede2/software/samtools-1.9/samtools flagstat "+name+"_0x43.bam")
os.system("/work/02114/wonaya/stampede2/software/samtools-1.9/samtools flagstat "+name+"_0x83.bam")
os.system("/work/02114/wonaya/stampede2/software/samtools-1.9/samtools view -h -o "+name+"_0x43.sam "+name+"_0x43.bam")
os.system("/work/02114/wonaya/stampede2/software/samtools-1.9/samtools view -h -o "+name+"_0x83.sam "+name+"_0x83.bam")

### filter 43 and search 83
outfile = open(name+"_0x43_mapqbelow10.sam", 'w')
for a in open(name+"_0x43.sam",'r'):
    if a[0] != "@" : 
        if float(a.split("\t")[4]) <= 10 :
            outfile.write(a)
    else :
        outfile.write(a)
outfile.close()

readID=[]
mapq=[]
for a in open(name+"_0x43_mapqbelow10.sam", 'r'):
    if a[0] != "@" :
        readID.append(a.split("\t")[0])
        mapq.append(float(a.split("\t")[4]))

second_mapq= []
for b in open(name+"_0x83.sam", 'r') :
    if b[0] != "@" : 
        if b.split("\t")[0] in readID :
            second_mapq.append(float(b.split("\t")[4]))

### filter 83 and search 43
outfile = open(name+"_0x83_mapqbelow10.sam", 'w')
for a in open(name+"_0x83.sam",'r'):
    if a[0] != "@" : 
        if float(a.split("\t")[4]) <= 10 :
            outfile.write(a)
    else :
        outfile.write(a)
outfile.close()

readID=[]
for a in open(name+"_0x83_mapqbelow10.sam", 'r'):
    if a[0] != "@" :
        readID.append(a.split("\t")[0])
        mapq.append(float(a.split("\t")[4]))

for b in open(name+"_0x43.sam", 'r') :
    if b[0] != "@" : 
        if b.split("\t")[0] in readID :
            second_mapq.append(float(b.split("\t")[4]))

## get distribution of p-values

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

bins = np.linspace(0, 60, 50)
plt.hist([mapq,second_mapq], bins, alpha=0.5, label=['first','second'])
plt.legend(loc='upper right')
#plt.show()
plt.savefig(name+"_mapqlessthan10pair.png")
