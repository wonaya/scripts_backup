import os,sys
import subprocess

bam = sys.argv[1]

count = 0

count += int(subprocess.check_output("samtools view "+bam+" 1:136770000-137120000 | wc -l", shell=True))
count += int(subprocess.check_output("samtools view "+bam+" 2:95510000-97490000 | wc -l", shell=True))
count += int(subprocess.check_output("samtools view "+bam+" 3:85780000-86930000 | wc -l", shell=True))
count += int(subprocess.check_output("samtools view "+bam+" 4:109070000-110500000 | wc -l", shell=True))
count += int(subprocess.check_output("samtools view "+bam+" 5:104540000-106820000 | wc -l", shell=True))
count += int(subprocess.check_output("samtools view "+bam+" 6:52300000-53110000 | wc -l", shell=True))
count += int(subprocess.check_output("samtools view "+bam+" 7:56380000-56680000 | wc -l", shell=True))
count += int(subprocess.check_output("samtools view "+bam+" 8:50530000-52070000 | wc -l", shell=True))
count += int(subprocess.check_output("samtools view "+bam+" 9:53750000-55390000 | wc -l", shell=True))
count += int(subprocess.check_output("samtools view "+bam+" 9:57360000-57760000 | wc -l", shell=True))
count += int(subprocess.check_output("samtools view "+bam+" 10:51390000-52780000 | wc -l", shell=True))

print int(count)


