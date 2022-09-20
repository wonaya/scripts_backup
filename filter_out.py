import os,sys

outfile = open("merged_all_log2_higherthan1_2.txt", 'w')
#for a in open("merged_all_log2_higherthan1.txt",'r') :
b = open("merged_all_log2.txt",'r')
c = b.readlines()
outfile.write(c[0])
for a in c[1:]:
    if any(float(t) < 1 for t in a.strip("\n").split("\t")[1:]) :
        continue
    else :
        outfile.write(a)
outfile.close()
