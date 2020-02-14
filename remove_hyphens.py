# 

import sys

fh = open(sys.argv[1])



for line in fh:
    if line[0] == ">":
       print line.strip()
       continue
    mystr = ''
    for i in range(0,len(line.strip())):
       if line[i] != '-':
           mystr += line[i]
    print mystr 


