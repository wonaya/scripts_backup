import os,sys

list_1 = []
for a in open(sys.argv[1], 'r' ) :
    list_1.append(a.strip("\n"))
list_2 = []
for a in open(sys.argv[2], 'r' ) :
    list_2.append(a.split("\t"))

count = 0
for b in list_1 :
    if b in list_2 : 
        count += 1
print count, "/", len(list_1)
print len(list_2)

