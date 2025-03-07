import sys
import heapq
# from datetime import datetime

def ParseFasta(filename):
    # 서열을 sequence로 읽자
    with open(filename, 'r') as file:
        sequence = "".join(line.strip() for line in file if not line.startswith(">"))
    return sequence

def KeepValidBases(sequence):
    return ''.join(base for base in sequence if base in 'ATGC')

def CountKmers(sequence, k):
    counts = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        counts[kmer] = counts.get(kmer, 0) + 1  
    return counts

def SaveTopKmers(kmerCounts, studentId):
    minHeap = []  

    for kmer, count in kmerCounts.items():
        entry = (count, kmer)

        if len(minHeap) < 100:
            heapq.heappush(minHeap, entry)
        elif count > minHeap[0][0] or (count == minHeap[0][0] and kmer > minHeap[0][1]):
            heapq.heappushpop(minHeap, entry)

    # 내림차순 정렬
    sortedTopKmers = sorted(minHeap, key=lambda x: (-x[0], x[1]))

    outputFile = f"{studentId}.txt"
    lastCount = sortedTopKmers[-1][0] 

    with open(outputFile, 'w') as file:
        file.writelines(f"{kmer},{count}\n" for count, kmer in sortedTopKmers)

        file.writelines(f"{kmer},{count}\n" for kmer, count in kmerCounts.items()
                        if count == lastCount and (count, kmer) not in minHeap)

def main():
    # starttime = datetime.now()
    k = int(sys.argv[1])  
    inputFile = sys.argv[2] 

    studentId = "202312753"
    dnaSeq = ParseFasta(inputFile)  
    validSeq = KeepValidBases(dnaSeq)  
    kmerCounts = CountKmers(validSeq, k)  
    SaveTopKmers(kmerCounts, studentId)  
    # print(datetime.now() - starttime)

if __name__ == "__main__":
    main()
