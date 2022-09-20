import os,sys


for a in open(sys.argv[1],'r') :
    if a.split("\t")[-2] != "" :
        print a.split("\t")[-2]


