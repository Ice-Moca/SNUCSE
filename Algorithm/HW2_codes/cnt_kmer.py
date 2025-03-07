import sys
from collections import defaultdict
import re
from multiprocessing import Pool, cpu_count

def read_and_clean_fasta(file_path):
    """
    Reads a FASTA file and removes non-ATGC characters in a single pass.
    """
    with open(file_path, 'r') as file:
        sequence = []
        for line in file:
            if line.startswith(">"):  # Skip headers
                continue
            sequence.append(re.sub('[^ATGC]', '', line.strip().upper()))
    return ''.join(sequence)

def count_kmers(sequence, k):
    """
    Efficiently counts k-mers using a sliding window approach.
    """
    kmer_counts = defaultdict(int)
    current_kmer = sequence[:k]
    kmer_counts[current_kmer] += 1
    for i in range(k, len(sequence)):
        current_kmer = current_kmer[1:] + sequence[i]  # Slide the window
        kmer_counts[current_kmer] += 1
    return kmer_counts

def merge_counters(counter1, counter2):
    """
    Merges two k-mer frequency dictionaries.
    """
    for kmer, count in counter2.items():
        counter1[kmer] += count
    return counter1

def process_chunk(args):
    """
    Processes a chunk of the sequence in parallel.
    """
    sequence, k = args
    return count_kmers(sequence, k)

def get_top_kmers(counter, top_n):
    """
    Gets the top N k-mers, sorted by count (desc) and alphabetically for ties.
    """
    sorted_kmers = sorted(counter.items(), key=lambda x: (-x[1], x[0]))  # Count desc, then k-mer alphabetically
    top_kmers = sorted_kmers[:top_n]
    
    # Handle ties for the last rank
    if len(sorted_kmers) > top_n:
        last_count = top_kmers[-1][1]
        additional_kmers = [item for item in sorted_kmers[top_n:] if item[1] == last_count]
        top_kmers += sorted(additional_kmers, key=lambda x: x[0])  # Alphabetical for ties
    
    return top_kmers

def main(file_path, k, top_n, use_multiprocessing=True):
    """
    Main function to compute top k-mers efficiently.
    """
    sequence = read_and_clean_fasta(file_path)
    
    if use_multiprocessing and len(sequence) > 10_000_000:  # Use multiprocessing for large sequences
        num_chunks = cpu_count()
        chunk_size = len(sequence) // num_chunks
        chunks = [(sequence[i * chunk_size:(i + 1) * chunk_size + k - 1], k) for i in range(num_chunks)]
        
        with Pool(num_chunks) as pool:
            counters = pool.map(process_chunk, chunks)
        
        # Merge all counters
        combined_counter = defaultdict(int)
        for counter in counters:
            combined_counter = merge_counters(combined_counter, counter)
    else:
        combined_counter = count_kmers(sequence, k)
    
    top_kmers = get_top_kmers(combined_counter, top_n)
    
    with open(fasta_file + "_" + str(k) + "mer_top1000.txt", 'w') as f:
        for kmer, count in top_kmers:
            f.write(f"{kmer},{count}\n")

# Example usage
if __name__ == "__main__":
#     fasta_file = "example.fna"  # Replace with your file path
    fasta_file = sys.argv[2]
#     k = 5  # Example k-mer size
    k = int(sys.argv[1])
    top_n = 1000  # Top k-mers
    main(fasta_file, k, top_n)
