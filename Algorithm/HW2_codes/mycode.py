import sys

def process_main(fasta_files, kmer_size, alpha_value):
    """
    FASTA 파일에서 LCS(Longest Common Subsequence)와 위치를 계산하고 결과를 저장
    
    Parameters:
        fasta_files (list): 비교할 두 FASTA 파일 경로 리스트
        kmer_size (int): k-mer의 크기
        alpha_value (float): k-mer 필터링 시 사용할 알파 값
    """
    # k-mer 필터링 수행
    filtered_kmers = filter_kmers(fasta_files, kmer_size, alpha_value)
    # k-mer 위치 찾기
    locations = find_kmers(fasta_files, filtered_kmers, kmer_size)
    # LCS 계산
    lcs, lcs_for_kmers1, lcs_for_kmers2 = find_lcs(locations)

    # 결과 파일 생성
    create_lcs_file(fasta_files, kmer_size, lcs)
    create_positions_file(fasta_files[0], kmer_size, lcs_for_kmers1)
    create_positions_file(fasta_files[1], kmer_size, lcs_for_kmers2)


def create_lcs_file(fasta_files, kmer_size, lcs):
    """
    LCS 결과를 파일로 저장
    
    Parameters:
        fasta_files (list): 비교한 두 FASTA 파일 이름
        kmer_size (int): k-mer의 크기
        lcs (list): 계산된 LCS 리스트
    """
    file_name = f"2023-12753_{kmer_size}_{fasta_files[0]}_{fasta_files[1]}_LCS.txt"
    with open(file_name, 'w') as file:
        result = '-'.join(lcs)
        file.write(result)


def create_positions_file(fasta_file, kmer_size, lcs_positions):
    """
    LCS의 위치 정보를 파일로 저장
    
    Parameters:
        fasta_file (str): FASTA 파일 이름
        kmer_size (int): k-mer의 크기
        lcs_positions (list): LCS에 포함된 k-mer와 위치 정보 리스트
    """
    file_name = f"2023-12753_{kmer_size}_{fasta_file}_LCS_positions.csv"
    with open(file_name, 'w', newline='') as file:
        for kmer, position in lcs_positions:
            file.write(f"{kmer},{position}\n")


def find_lcs(locations):
    """
    두 k-mer 집합에서 LCS를 계산
    
    Parameters:
        locations (list): 각 파일의 k-mer와 위치 정보 리스트
    
    Returns:
        tuple: (LCS 리스트, 첫 번째 파일의 LCS 위치 정보, 두 번째 파일의 LCS 위치 정보)
    """
    kmers1, kmers2 = locations[0], locations[1]
    len1, len2 = len(kmers1), len(kmers2)

    # DP 테이블 초기화
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # DP 테이블 계산
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if kmers1[i - 1][0] == kmers2[j - 1][0]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS 추적
    lcs, lcs_for_kmers1, lcs_for_kmers2 = [], [], []
    i, j = len1, len2
    while i > 0 and j > 0:
        if kmers1[i - 1][0] == kmers2[j - 1][0]:
            lcs.append(kmers1[i - 1][0])
            lcs_for_kmers1.append(kmers1[i - 1])
            lcs_for_kmers2.append(kmers2[j - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # LCS 결과 뒤집기
    return lcs[::-1], lcs_for_kmers1[::-1], lcs_for_kmers2[::-1]


def find_kmers(fasta_files, kmer_sets, kmer_size):
    """
    주어진 FASTA 파일에서 필터링된 k-mer를 찾rl
    
    Parameters:
        fasta_files (list): 비교할 두 FASTA 파일 경로 리스트
        kmer_sets (list): 필터링된 k-mer 세트
        kmer_size (int): k-mer의 크기
    
    Returns:
        list: 각 파일에서 찾은 k-mer와 위치 정보 리스트
    """
    return [find_each_kmer(fasta_files[i], kmer_sets[i], kmer_size) for i in range(2)]

def find_each_kmer(fasta_file, kmer_set, kmer_size):
    """
    FASTA 파일에서 주어진 k-mer를 검색하고 위치를 기록
    
    Parameters:
        fasta_file (str): FASTA 파일 경로
        kmer_set (set): 필터링된 k-mer 세트
        kmer_size (int): k-mer의 크기
    
    Returns:
        list: k-mer와 위치 정보 리스트
    """
    result = []
    sequence = []
    
    with open(fasta_file, 'r') as file:
        # 첫 번째 줄 건너뛰기
        next(file)
        for line in file:
            sequence.extend(line.strip())
    
    for i in range(len(sequence) - kmer_size + 1):
        candidate_kmer = ''.join(sequence[i:i + kmer_size])
        if candidate_kmer in kmer_set:
            result.append((candidate_kmer, i + 1))
    
    return result



def filter_kmers(fasta_files, kmer_size, alpha_value):
    """
    k-mer를 빈도수 및 중복 기준으로 필터링
    
    Parameters:
        fasta_files (list): FASTA 파일 경로 리스트
        kmer_size (int): k-mer의 크기
        alpha_value (float): 알파 값 (빈도 필터 기준)
    
    Returns:
        list: 필터링된 k-mer 세트 리스트
    """
    return [filter_each_kmer(fasta_files[i][:-6], kmer_size, alpha_value) for i in range(2)]


def filter_each_kmer(genome_name, kmer_size, alpha_value):
    """
    하나의 유전체 파일에서 k-mer를 필터링
    
    Parameters:
        genome_name (str): 유전체 파일 이름(확장자 제외)
        kmer_size (int): k-mer의 크기
        alpha_value (float): 알파 값 (빈도 필터 기준)
    
    Returns:
        set: 필터링된 k-mer 집합
    """
    result = set()
    freq_limit = 1000000 / (4 ** kmer_size) * alpha_value
    file_name = f"{genome_name}.fasta_{kmer_size}mer_top1000.txt"
    with open(file_name, 'r') as file:
        for line in file:
            kmer, count = line.strip().split(',')
            count = int(count)
            if count > freq_limit:
                continue
            if not any(is_overlapping(kmer, existing_kmer, kmer_size) for existing_kmer in result):
                result.add(kmer)
    return result


def is_overlapping(kmer1, kmer2, kmer_size):
    """
    두 k-mer가 기준 이상의 중첩을 가지는지 확인
    
    Parameters:
        kmer1 (str): 첫 번째 k-mer
        kmer2 (str): 두 번째 k-mer
        kmer_size (int): k-mer의 크기
    
    Returns:
        bool: 중첩 여부
    """
    # 기준 중첩 길이
    overlap_threshold = (kmer_size + 1) // 2  # 절반 이상이 중첩될 경우
    
    # 전방-후방 겹침 검사
    presuf_overlap = sum(1 for i in range(overlap_threshold) if kmer1[i] == kmer2[-overlap_threshold + i])
    if presuf_overlap >= overlap_threshold:
        return True

    # 후방-전방 겹침 검사
    sufpre_overlap = sum(1 for i in range(overlap_threshold) if kmer1[-overlap_threshold + i] == kmer2[i])
    if sufpre_overlap >= overlap_threshold:
        return True

    return False


if __name__ == '__main__':
    # 명령줄 인자 처리
    kmer_size = int(sys.argv[1])
    fasta_files = [sys.argv[2], sys.argv[3]]
    alpha_value = 1000000
    process_main(fasta_files, kmer_size, alpha_value)
