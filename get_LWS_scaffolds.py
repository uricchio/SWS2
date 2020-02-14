import sys


scaf = sys.argv[2]

fh = open(sys.argv[1],'r')

pr = 0
for line in fh:
    if line.strip() == scaf:
        pr = 1
        print line.strip()
        continue
    if pr ==1 and line[0] != ">":
        print line.strip()
    if line[0] == ">" and pr == 1:
        break
        
