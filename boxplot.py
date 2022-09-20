import os,sys

file = open(sys.argv[1],'r')
val = []
for a in file :
    val.append(float(a.split("\t")[-1]))
file = open(sys.argv[2],'r')
val2= []
for a in file :
    val2.append(float(a.split("\t")[-1]))


import matplotlib.pyplot as plt
import numpy as np

# fake up some data
data_to_plot = [val, val2]
fig=plt.figure(1, figsize=(9,6))
ax=fig.add_subplot(111)
bp= ax.boxplot(data_to_plot)
plt.show()
