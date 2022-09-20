import os,sys


## downsample
#os.system("java -jar /work2/02114/wonaya/software/picard.jar DownsampleSam I="+sys.argv[1]+" O=downsampled001.bam STRATEGY=ConstantMemory P=0.01 ACCURACY=0.0001")
#os.system("java -jar /work2/02114/wonaya/software/picard.jar DownsampleSam I="+sys.argv[1]+" O=downsampled005.bam STRATEGY=ConstantMemory P=0.05 ACCURACY=0.0001")
#os.system("java -jar /work2/02114/wonaya/software/picard.jar DownsampleSam I="+sys.argv[1]+" O=downsampled010.bam STRATEGY=ConstantMemory P=0.10 ACCURACY=0.0001")
#os.system("java -jar /work2/02114/wonaya/software/picard.jar DownsampleSam I="+sys.argv[1]+" O=downsampled025.bam STRATEGY=ConstantMemory P=0.25 ACCURACY=0.0001")
#os.system("java -jar /work2/02114/wonaya/software/picard.jar DownsampleSam I="+sys.argv[1]+" O=downsampled050.bam STRATEGY=ConstantMemory P=0.50 ACCURACY=0.0001")
## featurecount count how many genes have non-zero coverage
#os.system("/work2/02114/wonaya/software/subread/bin/featureCounts -a /work2/02114/wonaya/genome/maize/Zea_mays.AGPv5/Zea_mays.Zm-B73-REFERENCE-NAM-5.0.51.gtf -p -T 64 -t 'gene' -B --countReadPairs -g 'gene_id' -o featurecount001.txt downsampled001.bam")
#os.system("/work2/02114/wonaya/software/subread/bin/featureCounts -a /work2/02114/wonaya/genome/maize/Zea_mays.AGPv5/Zea_mays.Zm-B73-REFERENCE-NAM-5.0.51.gtf -p -T 64 -t 'gene' -B --countReadPairs -g 'gene_id' -o featurecount005.txt downsampled005.bam")
#os.system("/work2/02114/wonaya/software/subread/bin/featureCounts -a /work2/02114/wonaya/genome/maize/Zea_mays.AGPv5/Zea_mays.Zm-B73-REFERENCE-NAM-5.0.51.gtf -p -T 64 -t 'gene' -B --countReadPairs -g 'gene_id' -o featurecount010.txt downsampled010.bam")
#os.system("/work2/02114/wonaya/software/subread/bin/featureCounts -a /work2/02114/wonaya/genome/maize/Zea_mays.AGPv5/Zea_mays.Zm-B73-REFERENCE-NAM-5.0.51.gtf -p -T 64 -t 'gene' -B --countReadPairs -g 'gene_id' -o featurecount025.txt downsampled025.bam")
#os.system("/work2/02114/wonaya/software/subread/bin/featureCounts -a /work2/02114/wonaya/genome/maize/Zea_mays.AGPv5/Zea_mays.Zm-B73-REFERENCE-NAM-5.0.51.gtf -p -T 64 -t 'gene' -B --countReadPairs -g 'gene_id' -o featurecount050.txt downsampled050.bam")
#os.system("/work2/02114/wonaya/software/subread/bin/featureCounts -a /work2/02114/wonaya/genome/maize/Zea_mays.AGPv5/Zea_mays.Zm-B73-REFERENCE-NAM-5.0.51.gtf -p -T 64 -t 'gene' -B --countReadPairs -g 'gene_id' -o featurecount100.txt "+sys.argv[1])

##how many genes have non-zero coverage
list = []

count = 0
total = 0
for a in open("featurecount0001.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        if int(a.split("\t")[-1].strip("\n")) > 0 :
            count += 1
        total += 1
list.append(count)
print(total)

count = 0
for a in open("featurecount001.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        if int(a.split("\t")[-1].strip("\n")) > 0 :
            count += 1
        total += 1
list.append(count)

count = 0
for a in open("featurecount005.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        if int(a.split("\t")[-1].strip("\n")) > 0 :
            count += 1
        total += 1
list.append(count)

count = 0
total = 0
for a in open("featurecount010.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        if int(a.split("\t")[-1].strip("\n")) > 0 :
            count += 1
        total += 1
list.append(count)
print(total)

count = 0
total = 0
for a in open("featurecount025.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        if int(a.split("\t")[-1].strip("\n")) > 0 :
            count += 1
        total += 1
list.append(count)
print(total)

count = 0
total = 0
for a in open("featurecount050.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        if int(a.split("\t")[-1].strip("\n")) > 0 :
            count += 1
        total += 1
list.append(count)
print(total)

count = 0
total = 0
for a in open("featurecount100.txt", 'r') :
    if a[0] != "#" and a[0] != "G" :
        if int(a.split("\t")[-1].strip("\n")) > 0 :
            count += 1
        total += 1
list.append(count)
print(total)
print(list)
