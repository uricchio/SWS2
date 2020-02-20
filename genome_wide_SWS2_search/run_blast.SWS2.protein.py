import sys
import os

# location of blast on your machine
blast_DB_loc = '/usr/local/ncbi/blast/bin/tblastn'

# arguments to blast
arg0 = '-query infiles/SWS2_example.protein.fasta'
arg1 = '-db '+sys.argv[1]
arg2 = '-out output/SWS2_results.'+sys.argv[2]+'.tblastn.txt -outfmt '+sys.argv[2]

command = blast_DB_loc+' '
command += arg0+' '
command += arg1+' '
command += arg2

#run blast on sequence
os.system(command)

