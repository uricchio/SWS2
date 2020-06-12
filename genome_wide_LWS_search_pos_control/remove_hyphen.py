##

import sys

fh = open(sys.argv[1], 'r')

for line in fh:
    if line[0] == ">":
        print(line.strip())
        continue
    data = line.strip()
    out = ''
    for char in data:
        if char != "-":
            out += char 
    print (out)


