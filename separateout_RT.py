import os,sys

outfile = open("ratio_MS.bed", 'w')
for a in open("ratio_segmentation.bed", 'r') :
    if a.split("\t")[-1].split(";")[1] == "Name=MS" :
        outfile.write(a)
outfile.close()

outfile = open("ratio_ES.bed", 'w')
for a in open("ratio_segmentation.bed", 'r') :
    if a.split("\t")[-1].split(";")[1] == "Name=ES" :
        outfile.write(a)
outfile.close()

outfile = open("ratio_LS.bed", 'w')
for a in open("ratio_segmentation.bed", 'r') :
    if a.split("\t")[-1].split(";")[1] == "Name=LS" :
        outfile.write(a)
outfile.close()

outfile = open("ratio_ESMS.bed", 'w')
for a in open("ratio_segmentation.bed", 'r') :
    if a.split("\t")[-1].split(";")[1] == "Name=ESMS" :
        outfile.write(a)
outfile.close()

outfile = open("ratio_MSLS.bed", 'w')
for a in open("ratio_segmentation.bed", 'r') :
    if a.split("\t")[-1].split(";")[1] == "Name=MSLS" :
        outfile.write(a)
outfile.close()

outfile = open("ratio_ESMSLS.bed", 'w')
for a in open("ratio_segmentation.bed", 'r') :
    if a.split("\t")[-1].split(";")[1] == "Name=ESMSLS" :
        outfile.write(a)
outfile.close()

outfile = open("ratio_ESLS.bed", 'w')
for a in open("ratio_segmentation.bed", 'r') :
    if a.split("\t")[-1].split(";")[1] == "Name=ESLS" :
        outfile.write(a)
outfile.close()

