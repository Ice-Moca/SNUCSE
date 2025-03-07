#!/bin/bash
# Usage: sh run.sh 17 genome1.fasta genome2.fasta

k=$1
genome1=$2
genome2=$3

# Step 1: Run cnt_kmer.py for both genomes
python3 cnt_kmer.py $k $genome1 > ${genome1}_kmers.csv
python3 cnt_kmer.py $k $genome2 > ${genome2}_kmers.csv

# Step 2: Run mycode.py to calculate LCS and save results
python3 mycode.py $k $genome1 $genome2
