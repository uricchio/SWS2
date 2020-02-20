import sys
import os

# location of blast on your machine
blast_DB_loc = '/usr/local/ncbi/blast/bin/tblastn'

# arguments to blast
arg0 = '-query output/SWS2_in_tree.noHyph.With_tblastn.translated.fasta'
arg1 = '-db '+sys.argv[1]
arg2 = '-out output/Gene_annot_results.'+sys.argv[2]+'.tblastn.txt -outfmt '+sys.argv[2]

command = blast_DB_loc+' '
command += arg0+' '
command += arg1+' '
command += arg2

#run blast on sequence
os.system(command)

