#

import sys

# first argument should be a file with the output of tblastn in format 6
# second file should be the rna.fa file, which contains all the gene 
# annotations for nanorana

fh = open(sys.argv[1],'r')

gene_matches = {}

for line in fh:
    data = line.strip().split()
     
    # get lowest e-value match for each gene/sequence
    # find out what that sequence is     

    if data[0] not in gene_matches:
        gene_matches[data[0]] = [data[1], float(data[10])]
    elif data[0] in gene_matches and float(data[10]) < gene_matches[data[0]][1]:
        gene_matches[data[0]] = [data[1],float(data[10])]
    
fh.close()

fh = open(sys.argv[2])

gene_names = {}

for line in fh:
    for gene in gene_matches:
        if gene_matches[gene][0] in line.strip():
            gene_names[gene] = line.strip().split('|')[4][1:]

for gene in gene_matches:
    print (gene+'\t'+gene_matches[gene][0]+'\t'+str(gene_matches[gene][1])+'\t'+gene_names[gene] )


