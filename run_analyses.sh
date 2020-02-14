#!/bin/bash

# runs all analyses for detection of putative SWS2 pseudogene in Oophaga genome

# the first step is to make a database out of the Oophaga genome assembly
# we are not able to distribute this data, so please download the data from 
# https://academic.oup.com/mbe/article/35/12/2913/5106668
# gunzip the file Oophaga.clean.newest.fa.gz and put it in pumilio data,
# then uncomment the next command and run it
 
# Make blast db
python make_blast_db.py pumilio_data/Oophaga.clean.newest.fa 0

# running blast to determine the scaffold that contains LWS
python run_blast.py OophagaDB/Oophaga.0 0 6

# find LWS scaffold at 1e-20 threshold
var=$(cat output/LWS_results.0.6.txt | awk '{if($11 < 1e-20) print $2}')

# find LWS 
python  get_LWS_scaffolds.py pumilio_data/Oophaga.clean.newest.fa $var > output/LWS_scaffold.fa
