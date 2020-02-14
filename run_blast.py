import sys
import os

if len(sys.argv) < 4:
    print 'usage: python ', sys.argv[0], '<blast_data_base_name> <index_for_output_file> <format_index>' 
    exit() 

blast_DB_loc = '/usr/local/ncbi/blast/bin/blastn'

arg0 = '-query infiles/LWS_in_tree.noHyph.fasta'
arg1 = '-db '+sys.argv[1]
arg2 = '-out output/LWS_results.'+sys.argv[2]+'.'+sys.argv[3]+'.txt'
arg3 = ' -outfmt '+sys.argv[3]

command = blast_DB_loc+' '
command += arg0+' '
command += arg1+' '
command += arg2+' '
command += arg3

#run blast on sequence
os.system(command)


