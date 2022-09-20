import os,sys

outfile = open("trim_all.txt", 'w')
for ROOT,DIR,FILES in os.walk("."):
    for file in FILES:
       if file.endswith(('_R1_001.fastq')):
          file_id = "_".join(file.split("_")[:3])
          barcode = file.split("_")[1]
          print file_id, barcode
          outfile.write("/work/02114/wonaya/software/trim_galore --fastqc -a GATCGGAAGAGCACACGTCTGAACTCCAGTCAC"+barcode+"ATCTCGTATGCCGTCTTCTGCTTG -a2 GATCGGAAGAGCACACGTCTGAACTCCAGTCAC"+barcode+"ATCTCGTATGCCGTCTTCTGCTTG -t --paired "+file_id+"_R1_001.fastq "+file_id+"_R2_001.fastq")
          outfile.write("\n")
outfile.close()