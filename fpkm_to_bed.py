import os,sys

outfile = open(sys.argv[2], 'w') 
for a in open(sys.argv[1], 'r') :
    if a.split("\t")[0] != "tracking_id" :
        outfile.write(a.split("\t")[6].split(":")[0])
        outfile.write("\t")
        outfile.write(a.split("\t")[6].split(":")[1].split("-")[0])
        outfile.write("\t")
        outfile.write(a.split("\t")[6].split(":")[1].split("-")[1])
        outfile.write("\t")
        outfile.write(a.split("\t")[9])
        outfile.write("\t")
        outfile.write(a.split("\t")[0]+"\n")
outfile.close()

