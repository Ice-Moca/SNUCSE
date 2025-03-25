# HW1: K-mer counting and sorting (Modified Oct 28)

---

Dear Students,

The k-mer counting homework assignment is now live. You are required to write a Python or Java program that counts k-mers in the E. coli DNA sequence, with results sorted alphabetically. Read the attached HW instruction file carefully and submit your files in `.zip` file, containing a `run.sh` file. Please ensure that you **test your code on the provided server** using your assigned account to guarantee compatibility and performance, as the algorithm will be graded based on the correctness of your answer and run time. Your server accounts are provided in the excel file.

The submission is due by **November 7, 23:59, with no late submissions unless prior approval**. Make sure your output file strictly follows the required format to avoid penalties.

Happy coding!

+ Added 10/10 11:12AM:

To simplify the bit encoding scheme, we limit the value k of k-mer as below 16 for testing.

Also, we clarify that for this assignment, you are allowed to use only **pre-built packages** (such as Python’s `math` and `os` libraries). We want to clarify that **Java’s `java.io` package** (e.g., `BufferedReader`, `FileReader`) is part of the core Java libraries, and thus, you are allowed to use it. The restriction only applies to third-party packages that are not part of the Python Standard Library or Java Standard Library that requires additional installation process.

+ Added 10/15 3:04PM:

We have noticed there are characters other than 'A','C','G','T' in the sequences. Please treat them just like 'N', and remove them from the sequence such that after processing, 'ATNT' becomes 'ATT'.

+ Added 10/21 11:15AM:

Regarding the final zip file, name them as `[student_number].zip`. Also, the input file in "*Submit your Python/Java code, the input file, and your “run.sh” script in a single zip file in ETL*" refers to input files (e.g. compiled java files) related to your codes, **not the sequence files**. Please remember that codes should run on any test file that the grader inputs  as arguments.

+ Added 10/28 4:38 PM:

**Output 파일 변경**

- Output file은 이제 전체 k-mer을 string으로 sorting한 결과가 아닌, **count 로 sorting 한 후 상위 100개의 k-mer 및 그 갯수를 나열**해야 합니다.
- 공동등수가 발생할 경우 k-mer을 alphabetical order로 sorting하여 출력해야 합니다.
- 100등에서 같은 count 값이 발생할 경우 공동 100등인 k-mer을 alphabetical order로 sorting하여 output file에 작성해주시기 바랍니다.

Thanks to the students who discovered the problem of the homework. For further inquiries please contact TA: [eugenomics@snu.ac.kr](mailto:eugenomics@snu.ac.k).

**Attached files: [SNU2024Fall_Algorithm_HW1.zip](https://myetl.snu.ac.kr/courses/268021/files/5121125/download?wrap=1)**

*SNU2024Fall_Algorithm_HW1.pdf* : HW1 instruction file

*2024Alg_server_id.xlsx* : Server account and login information

*Nonpathogenic_Escherichia coli ATCC 25922.fna* : Example sequence file 1

*Pathogenic_Escherichia coli O104H4.fna* : Example sequence file 2
