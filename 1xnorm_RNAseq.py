import os,sys
from collections import defaultdict 
from operator import itemgetter
# python RNAseq_1xnorm.py bamfile genome_size read_length

files = sys.argv[1]
name=files.split(".bam")[0]
#os.system("export LC_ALL=C; bedtools bamtobed -i %s | cut -f 1-3 | sort -S 1G -k1,1 -k2,2n > %s"%(files, name+".bed"))
#os.system("bedtools intersect -a %s -b %s -c -sorted > %s"%("maize_4.33_w1000.bed", name+".bed", name+".bedgraph"))
outfile = open(name+"_1xnorm.bedgraph", 'w')
BGF = open(name+".bedgraph", 'r')
noComments = filter(lambda x: x[0] != '#', BGF)
genome = defaultdict(list)
# Read Data
for line in noComments:
    tmp = line.rstrip('\n').split('\t')
    s, e, v = int(tmp[1]), int(tmp[2]), float(tmp[3])
    genome[tmp[0]].append((s,e,v))
## Calculate scaling factor
total_reads = 0
for a in open(name+".bedgraph", 'r') :
    total_reads += float(a.split("\t")[-1].strip("\n"))
print "total reads", total_reads
scale = 1/(total_reads*float(sys.argv[3])/float(sys.argv[2]))
print "scale", scale
sChroms = sorted(genome.keys())
for chrom in sChroms:
    for record in genome[chrom]:
	s, e, v = record
	oV = v*scale
	if int(oV) == oV:
	    outfile.write('%s\t%i\t%i\t%i\n'%(chrom, s, e, oV))
	else:
            outfile.write('%s\t%i\t%i\t%.3f\n'%(chrom, s, e, oV))
outfile.close()

