#!/bin/bash

# runs all analyses for detection of putative SWS2 pseudogene in Oophaga genome
# you will need to have BLAST and mafft installed for these analyses

# the first step is to make a database out of the Oophaga genome assembly
# we are not able to distribute this data, so please download the data from 
# https://academic.oup.com/mbe/article/35/12/2913/5106668
# gunzip the file Oophaga.clean.newest.fa.gz and put it in the folder pumilio_data
 
# Make blast db
python make_blast_db.py pumilio_data/Oophaga.clean.newest.fa 0

# running blast to determine the scaffold that contains LWS
python run_blast.py OophagaDB/Oophaga.0 0 6

# find LWS scaffold at 1e-20 threshold
myvar=$(cat output/LWS_results.0.6.txt | awk '{if($11 < 1e-20) print $2}'| sort | uniq)

# find LWS and reverse complement
python get_LWS_scaffolds.py pumilio_data/Oophaga.clean.newest.fa $myvar > output/LWS_scaffold.fa

# make input file and align LWS scaffold to nanorana and known SWS2 sequences/LWS sequences
cat infiles/LWS_example_seq.fa > infiles/mafft.input.fa
cat output/LWS_scaffold.fa >> infiles/mafft.input.fa
cat infiles/nanorana_LWS_SWS2_seq.fa >> infiles/mafft.input.fa
cat infiles/SWS2_example_seq.fa >> infiles/mafft.input.fa

# We tried many different options within mafft.  While these have a big effect on the 
# reported alignments, generally none of these changes resulted in compelling candidate
# SWS2 sequences in the Oophaga genome assembly

# we used  MAFFT v7.453 (2019/Nov/8)
# https://mafft.cbrc.jp/alignment/software/
mafft --ep 1 infiles/mafft.input.fa > output/mafft.aligned_scaffolds.fa

# if you wish to visualize the alignments you can use UGENE or another viewer, http://ugene.net/
