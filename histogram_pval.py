## histogram

import os,sys

## get distribution of p-values

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

x = []
for a in open(sys.argv[1], 'r') :
    if a[:2] != '"b' :
        if a.split("\t")[-1].strip("\n") !=  "NA" :
            #x.append(float(a.split("\t")[-1].strip("\n")))
            x.append(float(a.split("\t")[2]))
#plt.xscale('log')
plt.yscale('log')
plt.hist(x, 100, facecolor='green', alpha=0.75)
#plt.xlabel("adj p-val")
plt.xlabel("log2FC")
plt.ylabel("count")
plt.show()
