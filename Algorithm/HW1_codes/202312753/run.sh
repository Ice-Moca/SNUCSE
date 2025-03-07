#!/bin/bash

KMER_LENGTH=$1
INPUT_FILE=$2

python3 your_program.py "$KMER_LENGTH" "$INPUT_FILE"

echo "K-mer counting completed. Please check the output file."