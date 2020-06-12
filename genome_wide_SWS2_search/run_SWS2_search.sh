#!/bin/bash

# make protein sequences from nucloetide fasta
python2 translate_fasta.py infiles/SWS2_in_tree.noHyph.fasta > output/SWS2_in_tree.noHyph.With_tblastn.translated.fasta

# run a blast on the SWS2 sequences using the Oophaga databse
python2 run_blast.SWS2.protein.py ../synteny/OophagaDB/Oophaga.0 7 

# make a fasta that nw includes the results of the blast search, using hits with evals < 1e-10
python2 make_fasta_from_tblastn7.py 1e-10 output/SWS2_results.7.tblastn.txt ../synteny/pumilio_data/Oophaga_pumilio_P_RNA-scaffolded_genome.fasta >> output/SWS2_in_tree.noHyph.With_tblastn.translated.fasta 

# align results of BLAST to SWS2 sequences
mafft  output/SWS2_in_tree.noHyph.With_tblastn.translated.fasta  >  output/SWS2_in_tree.noHyph.With_tblastn.translated.mafft.fasta 

# visualize alignments in UGENE or similar viewer if desired.

# change directory to wherever raxML is on your machine
#cd ~/projects/pop_gen_software/standard-RAxML-master
#./raxmlHPC-SSE3 -m PROTGAMMALGF -s ~/projects/poison/LWS_blast/SWS2_in_tree.noHyph.With_tblastn.translated.mafft.fasta -p 12345 -n treeAllSeqs
# this tree will probably not look great because the alignments are not highly tuned -- we tried several different approaches (largely changing
# the options in mafft and subsetting the aligments down to the regions of highest sequence similarity), but none of the trees suggested that
# any of the candidate sequences were likely to be SWS2 pseudogenes

# check for orhologs using blast with nanorana
python2 run_blast.nanorana.py nanoranaDB/nanorana.0 6

# get best matching blast hit for each tblastn against Oophaga
python2 get_putative_ortholog_names.py output/Gene_annot_results.6.tblastn.txt infiles/rna.fa > output/most_similar_gene_in_nanorana.txt
