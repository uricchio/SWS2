import sys
import os

if len(sys.argv) < 3:
    print "please provide input file name for BLAST db and index number"
    print "input file is a fasta with the genome assembly, e.g., Oophaga.fa"
    exit()

# SET TO BLAST LOCATIOMN ON YOUR MACHINE
blast_DB_loc = '/usr/local/ncbi/blast/bin/makeblastdb'
i = sys.argv[2]

arg1 = '-out nanoranaDB/nanorana.'+i
arg2 = '-dbtype nucl'
arg3 = '-in '+sys.argv[1]

command = blast_DB_loc+' '
command += arg1+' '
command += arg2+' '
command += arg3

#first make blast directory from pumilo genome
os.system(command)

