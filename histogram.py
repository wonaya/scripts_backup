## histogram

import os,sys

## get distribution of p-values

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
x = []
for a in open(sys.argv[1], 'r') :
    x.append(float(a.strip("\n")))
for a in open(sys.argv[2], 'r') :
    x.append(float(a.strip("\n")))
#for a in open(sys.argv[3], 'r') :
#    x.append(float(a.strip("\n")))
y = []
for a in open(sys.argv[3], 'r') :
    y.append(float(a.strip("\n")))
for a in open(sys.argv[4], 'r') :
    y.append(float(a.strip("\n")))
#for a in open(sys.argv[6], 'r') :
#    y.append(float(a.strip("\n")))

#x = np.asarray(x)
#y = np.asarray(y)
#z= np.column_stack((x,y))
bins = np.linspace(0, 100, 50)
#fig, axes = plt.subplot(nrows=1, ncols=1)
#ax0 = axes.flatten()
#labels= ['original','rmdup']
#ax0.hist(z, n_bins, density=True, histtype='bar', color=['blue','green'], label=colors)
#ax0.legend(prop={'size': 10})
#plt.savefig("test.jpg")
plt.hist([x,y], bins, alpha=0.5, label=['all','rm'])
plt.legend(loc='upper right')
#plt.savefig("test.png")
plt.show()
#plt.hist(x, 50, facecolor='green', alpha=0.5)
#plt.hist(y, 50, facecolor='blue',alpha=0.5)
#plt.show()

