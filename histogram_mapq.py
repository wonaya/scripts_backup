## histogram

import os,sys

## get distribution of p-values

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = []
for a in open(sys.argv[1], 'r') :
    if a[0] != "@" : 
        x.append(float(a.split("\t")[4]))
plt.yscale('log', nonposy='clip')
plt.hist(x, 50, facecolor='green', alpha=0.75)
plt.savefig(sys.argv[1].strip(".sam")+"_mapq_hist.png")
