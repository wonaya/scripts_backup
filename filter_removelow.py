import os,sys

#make gene dict
genedict = {}
for a in open("merge_featurecount.txt", 'r') :
    if a[0] != "G" :
        genedict[a.split("\t")[0]] = []
#add in values
for a in open("merge_featurecount.txt", 'r') :
    if a[0] != "G" :
        for x in a.split("\t")[1:] : 
            genedict[a.split("\t")[0]].append(float(x.strip("\n")))
#filter if at least one
total = [0]*8
for a in genedict.keys() :
    if a[0] != "G" :
        index = 0
        for b in genedict[a]:
            total[index] += b 
            index += 1
print total ; sys.exit()
print len(genedict)
for a in genedict.keys() :
    if 0 in genedict[a] : 
        del genedict[a]
print len(genedict)

import numpy
#get 0.25 cutoff
alllist = []
for a in genedict.keys() :
    for b in genedict[a] :
        alllist.append(b)
print alllist[:10]
print numpy.percentile(alllist, 2.5)

import matplotlib.pyplot as plt

fig = plt.figure(figsize =(10, 7))
plt.boxplot(alllist)
plt.show()
