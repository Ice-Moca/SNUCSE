# HW2: Genome Alignment (수정 11/24 17:30)

---

안녕하세요.

HW #2에 대한 세부 내용을 안내드립니다. 과제는 주어진 두 유전체 서열을 정렬(Alignment)하고 Longest Common Subsequence (LCS)를 찾아내는 작업으로 구성되어 있습니다. 자세한 내용은 첨부된 과제 파일을 참고해 주세요.

**과제 목표**

1. k-mer 필터링 기준을 세워 k-mer를 선정하고, 두 유전체를 다시 스캔하여 선정된 k-mer의 발생 위치를 기록합니다.

2. Dynamic Programming 기반 알고리즘을 사용하여 두 유전체 간 LCS를 계산합니다.

3. 결과를 아래 세 가지 파일 형식으로 저장합니다.

**과제 제출 방법**

Python 또는 Java로 코드 작성 후, 실행 스크립트(run.sh)와 함께 하나의 zip 파일로 압축하여 제출하세요.

파일명 예: 2024-00001.zip

제출 파일은 반드시 첨부된 Expected Output Format과 Submission Guidelines를 준수해야 합니다.

**주의 사항**

1. 적절한 Overlapping과 Too Frequent 기준을 마련하여 k-mer 필터링을 수행하세요.

2. 출력 파일에는 LCS 서열뿐만 아니라 각 k-mer의 위치 정보가 포함되어야 합니다.

3. 코드는 주어진 실행 명령어에 따라 정상 작동해야 하며, 예시로 주어진 genome files 외에 다른 genome files로 실행 시간 및 정확도를 평가합니다.

4. 반드시 제공된 서버에서 할당된 계정을 사용하여 코드를 테스트해 주세요. 호환성과 성능 보장을 위해 서버에서 실행 여부를 확인해야 합니다. 서버 계정 정보는 HW1 공지 시 제공된 내용을 참고하세요.

5. 허용된 library만 사용 가능합니다. Python에서는 math, os와 같은 standard library만 사용 가능합니다. Java에서는 java.io (예: BufferedReader, FileReader)와 같은 Java Standard Library의 기본 package 사용이 허용됩니다. 제한: Python Standard Library나 Java Standard Library 외의 추가 설치가 필요한 third-party package는 사용할 수 없습니다.

**제출 기한**

제출 마감: 2024-12-02 (시간: 23:59 KST)

마감 이후에는 제출이 허용되지 않습니다.

**첨부파일**

[SNU2024Fall_Algorithms_HW2_수정1.zip](https://myetl.snu.ac.kr/courses/268021/files/5509020/download?wrap=1)

질문이 있을 경우 Q&A 게시판을 이용해 주세요. (이메일로 문의는 받지 않습니다.)

**+ 11/18 Q&A**

- cnt_kmer.py 코드 내에서 출력하는 함수를 파일 write하도록 수정하셔도 됩니다.
- 제공드린 py 파일의 위치는 임의로 정해도 됩니다. 채점 시 제출하시는 run.sh을 실행시키기 위해서는 제공드린 py파일은 제출 시 반드시 포함되어야 할 것입니다.
- 발생 위치는 k-mer의 첫번째 nucleotide가 genome fasta file에서 몇 번째에 나타나는지를 의미합니다. Genome sequence가 AATGC**AGTC**ACTGCTGCTG이고 k-mer가 AGTC인 경우 발생위치는 6입니다.

**+ 11/22 Q&A**

- 발생 위치는 one-based index로 세면됩니다.
- ATGCatgc 이외의 문자도 고려하고 위치를 세야합니다. Genome sequence가 AATGN**AGTC**ACTGCTGCTG이고 k-mer가 AGTC인 경우, N이 5번째 위치에 있어도 AGTC의 발생위치는 6입니다.

**+ 11/24 Q&A**

- page 4와 5에서 제시된 파일명이 달라 수정되었습니다.

감사합니다.
