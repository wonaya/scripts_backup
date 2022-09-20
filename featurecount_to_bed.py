import os,sys

dict_tmm = {}
for a in open(sys.argv[1].strip(".txt")+".tmm.txt", 'r') :
    if a[0] != "\t" and a[0] != "0" and a[0] != "G" :
        dict_tmm[a.split("\t")[0]] = a.split("\t")[1].strip("\n")
outfile = open(sys.argv[2], 'w')
outfile2 = open(sys.argv[2].strip(".bed")+".tmm.bed", 'w')
for a in open(sys.argv[1], 'r') :
    if a[0] != "G" and a[0] != "#" :
        if len(a.split("\t")[2].split(";")) > 1 : 
            if len(set(a.split("\t")[1].split(";"))) > 1 : 
                print a ; sys.exit()
            else : 
                chr = a.split("\t")[1].split(";")[0] 
                start = str(min(map(float, (a.split("\t")[2].split(";")))))
                end = str(max(map(float,(a.split("\t")[3].split(";")))))
                outfile.write(chr+"\t"+start+"\t"+end+"\t"+a.split("\t")[-1].strip("\n")+"\t"+a.split("\t")[0]+"\t"+"\n")
                outfile2.write(chr+"\t"+start+"\t"+end+"\t"+dict_tmm[a.split("\t")[0]]+"\t"+a.split("\t")[0]+"\n")
        else :
            outfile.write(a.split("\t")[1]+"\t"+a.split("\t")[2]+"\t"+a.split("\t")[3]+"\t"+a.split("\t")[-1].strip("\n")+"\t"+a.split("\t")[0]+"\t"+"\n")
            outfile2.write(a.split("\t")[1]+"\t"+a.split("\t")[2]+"\t"+a.split("\t")[3]+"\t"+dict_tmm[a.split("\t")[0]]+"\t"+a.split("\t")[0]+"\n")
outfile.close()
outfile2.close()

os.system("/work2/02114/wonaya/software/bedtools2/bin/sortBed -i "+sys.argv[2]+" > "+sys.argv[2]+".sorted")
os.system("/work2/02114/wonaya/software/bedtools2/bin/sortBed -i "+sys.argv[2].strip(".bed")+".tmm.bed > "+sys.argv[2].strip(".bed")+".tmm.bed.sorted")
os.system("mv "+sys.argv[2]+".sorted "+sys.argv[2])
os.system("mv "+sys.argv[2].strip(".bed")+".tmm.bed.sorted "+sys.argv[2].strip(".bed")+".tmm.bedGraph")


