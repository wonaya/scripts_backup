import os,sys

outfile = open("test.sam", 'w')
for a in open(sys.argv[1],'r'):
    if a[0] != "@" : 
        if float(a.split("\t")[4]) <= 10 :
            outfile.write(a)
    else :
        outfile.write(a)
outfile.close()
