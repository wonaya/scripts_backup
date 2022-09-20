import os,sys

import numpy as np
import matplotlib.pyplot as plt

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []
data10 = []
data11 = []
data12 = []

for a in open("tpm.out" ,'r'): 
    if a.split("\t")[0] != "" :
        data1.append(float(a.split("\t")[1])) #BR1Seminal
        data2.append(float(a.split("\t")[2])) #BR2Primary
        data3.append(float(a.split("\t")[3])) #BR4Primary
        data4.append(float(a.split("\t")[4])) #BR3Primary
        data5.append(float(a.split("\t")[5])) #BR2Seminal
        data6.append(float(a.split("\t")[6])) #BR3Primary_Seminal
        data7.append(float(a.split("\t")[7])) #BR4Seminal
        data8.append(float(a.split("\t")[8])) #BR2Primary_Seminal
        data9.append(float(a.split("\t")[9])) #BR1Primary_Seminal
        data10.append(float(a.split("\t")[10])) #BR4Primary_Seminal
        data11.append(float(a.split("\t")[11])) #BR3Seminal
        data12.append(float(a.split("\t")[12].strip("\n"))) #BR1Primary

fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)
#ax4 = fig.add_subplot(231)
#ax5 = fig.add_subplot(232)
#ax6 = fig.add_subplot(233)
#ax7 = fig.add_subplot(331)
#ax8 = fig.add_subplot(332)
#ax9 = fig.add_subplot(333)
#ax10 = fig.add_subplot(431)
#ax11 = fig.add_subplot(432)
#ax12 = fig.add_subplot(433)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

#ax1.scatter(data12,data1, alpha=0.5)
#ax2.scatter(data1,data9, alpha=0.5)
#ax3.scatter(data12,data9, alpha=0.5)
#ax1.scatter(data2,data5, alpha=0.5)
#ax2.scatter(data5,data8, alpha=0.5)
#ax3.scatter(data2,data8, alpha=0.5)
#ax1.scatter(data4,data11, alpha=0.5)
#ax2.scatter(data11,data6, alpha=0.5)
#ax3.scatter(data4,data6, alpha=0.5)
ax1.scatter(data3,data7, alpha=0.5)
ax2.scatter(data7,data10, alpha=0.5)
ax3.scatter(data3,data10, alpha=0.5)

#ax.set_xlabel('common xlabel')
#ax.set_ylabel('common ylabel')

#ax1.set_title('BR1 Primary vs BR1 Seminal')
#ax2.set_title('BR1 Seminal vs BR1 Primary_Seminal')
#ax3.set_title('BR1 Primary vs BR1 Primary_Seminal')
#ax1.set_title('BR2 Primary vs BR2 Seminal')
#ax2.set_title('BR2 Seminal vs BR2 Primary_Seminal')
#ax3.set_title('BR2 Primary vs BR2 Primary_Seminal')
#ax1.set_title('BR3 Primary vs BR3 Seminal')
#ax2.set_title('BR3 Seminal vs BR3 Primary_Seminal')
#ax3.set_title('BR3 Primary vs BR3 Primary_Seminal')
ax1.set_title('BR4 Primary vs BR4 Seminal')
ax2.set_title('BR4 Seminal vs BR4 Primary_Seminal')
ax3.set_title('BR4 Primary vs BR4 Primary_Seminal')
plt.show()
