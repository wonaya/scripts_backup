import os,sys

source = []
seq = []
for a in open("Zm-B73-REFERENCE-NAM-5.0.TE.bed", 'r') :
    if a[0] != "#" :
        source.append(a.split("\t")[7])
        seq.append(a.split("\t")[6])

source = set(source)
seq = set(seq)

print source
print seq

for x in source : 
    file = open(x+".bed", 'w') 
    for y in open("Zm-B73-REFERENCE-NAM-5.0.TE.bed", 'r') : 
        if y.split("\t")[7] == x :
            file.write(y)
    file.close()

