# *nix system, everything is a file
# - Unix/Linux 시스템에서는 모든 것이 파일로 취급됨

# Unix I/O
/dev/sda # 디스크 장치 first disk on SATA bus
/dev/input/mice # 마우스 장치 aggregated of all connected mice
/dev/tty   # 터미널 장치 terminal

# kernel is exposed with a number of files
: '
kernel은 운영 체제의 핵심 부분으로, 하드웨어와 소프트웨어 간의 중간 역할을 수행하는 프로그램입니다. 
운영 체제의 가장 중요한 구성 요소로, 다음과 같은 주요 기능을 제공합니다:

프로세스 관리: 여러 프로그램이 동시에 실행될 수 있도록 프로세스를 생성, 스케줄링, 종료 등을 관리합니다.
메모리 관리: 시스템 메모리를 효율적으로 할당하고, 프로그램 간 메모리 충돌을 방지합니다.
파일 시스템 관리: 파일 및 디렉토리의 생성, 삭제, 읽기, 쓰기 등을 처리합니다.
장치 관리: 하드웨어 장치(예: 디스크, 네트워크 카드, 프린터 등)와 소프트웨어 간의 통신을 관리합니다.
시스템 호출 인터페이스: 사용자 프로그램이 커널 기능을 사용할 수 있도록 시스템 호출을 제공합니다.
'
/dev/kmem # 커널 메모리 kernel memory image, disaabled by Ubuntu by default
/proc # kernel data structures

# System configuration is mapped as files
/sys # system configuration
: '
# Unix File Types
# Regular file
- File containing user/app data(text, image, binary, etc.)
- OS does not know anything about the format(other than "sequence of bytes")

# Directory
- A file that contains the naames and locations (i-numbers) of files inside the directory

# Device file
- Character special file: process sequentilly, one chara at a time, devices that do not need random access 
ex) keyboard, mouse, terminal, sound card
- Block special file: process data in fixed-size blocks, devices that need random access 
ex) hard disk, USB drive, CD/DVD drive

# FIFO (named pipe)
- File type used for inter-process communication(exists only at memory unlike regular files)
- First In, First Out

# Socket
- File type used for inter-process communication
- Similar to FiFO files, but bidirectional communication even across networks

# Key Features
- Design concept: All input & output is handled in  a consistent and uniform way
- Elegant mapping of files to devices allow kernel to export simple interface called Unix I/O

'
mkfifo abc
gzip –c < abc > abc.gz&
cat document.txt > abc
rm abc

# ////////////////////////////////////////////////////////////////////////
: 'One root to rule them all
-mapped filesystems hide the contents of the directory tree under the mount point

single file system starting with at the root (“/”)
unlike Windows, there is no concept of a “drive”
additional filesystems are mapped into the file system tree as a directory 
mount point = directory where a filesystem is attached'
# //////////////////////////////////////////////////////////////////////// 

devel@caspvm $ ls -1
# 현재 디렉토리에 존재하는 폴더 목록을 확인
share
temp
work

devel@caspvm $ mkdir extern
# extern 폴더 생성

devel@caspvm $ echo "hello" > extern/hello
# extern 폴더 내부에 'hello'라는 파일을 생성하고 "hello"라는 내용을 입력

devel@caspvm $ ls extern/
# extern 폴더 내부 파일 목록 확인
hello

devel@caspvm $ sudo mount -t tmpfs /dev/shm extern/
# extern 폴더를 tmpfs (메모리 기반 임시 파일 시스템)로 마운트
# 이 작업을 수행하면 extern 폴더의 기존 내용이 보이지 않음
: '마운트 작업의 주요 개념
마운트 포인트 (Mount Point):

파일 시스템이 연결되는 디렉토리입니다. 예를 들어, /mnt 디렉토리에 파일 시스템을 마운트하면, /mnt 디렉토리 아래에서 해당 파일 시스템의 내용을 접근할 수 있습니다.
마운트 명령어:

mount 명령어를 사용하여 파일 시스템을 마운트합니다.
예시: sudo mount -t ext4 /dev/sda1 /mnt
/dev/sda1: 마운트할 디스크 파티션
/mnt: 마운트 포인트
-t ext4: 파일 시스템 타입 (여기서는 ext4)
언마운트 (Unmount):

마운트된 파일 시스템을 연결 해제하는 작업입니다.
umount 명령어를 사용합니다.
예시: sudo umount /mnt'

devel@caspvm $ ls extern/
# extern 폴더 내부를 다시 확인 -> 기존에 있던 hello 파일이 사라짐 (덮어씌워짐)

devel@caspvm $ echo "extern" > extern/extern
# extern 폴더 내부에 새 파일 'extern'을 생성하고 "extern"이라는 문자열을 입력

devel@caspvm $ ls extern/
# extern 폴더 내부 확인 -> 새로 만든 'extern' 파일만 존재
extern

devel@caspvm $ sudo umount extern
# extern 폴더에서 tmpfs 파일 시스템을 언마운트

devel@caspvm $ ls extern/
# extern 폴더 내부를 다시 확인 -> 원래 존재하던 'hello' 파일이 다시 나타남
hello

# ////////////////////////////////////////////////////////////////////////
devel@caspvm $ mount
/dev/sda4 on / type ext4 (rw,noatime)
# /dev/sda4 장치를 루트 파일 시스템 (/)로 마운트
# 파일 시스템 타입: ext4
# 옵션:
#   - rw: 읽기/쓰기 허용
#   - ro: do not allow write
#   - noatime: do not update access time
#   - noexec: do not allow execution
#   - nosuid: do not allow set-user-ID 

none on /tmp type tmpfs (rw,noatime,size=262144k)
# /tmp 디렉토리를 tmpfs (메모리 기반 파일 시스템)로 마운트
# 옵션:
#   - rw: 읽기/쓰기 허용
#   - noatime: 접근 시간 업데이트 방지
#   - size=262144k: 최대 256MB까지 사용 가능

none on /var/tmp type tmpfs (rw,noatime,size=131072k)
# /var/tmp 디렉토리도 tmpfs로 마운트, 최대 128MB 사용 가능

devel_share on /home/devel/share type vboxsf (rw,nodev,relatime,iocharset=utf8,uid=1000,gid=100)
# VirtualBox의 공유 폴더 (vboxsf 타입) 마운트
# 옵션:
#   - rw: 읽기/쓰기 허용
#   - nodev: 장치 파일 생성 금지
#   - relatime: 최근 접근 시간만 기록 (atime 업데이트 최적화)
#   - iocharset=utf8: UTF-8 문자 인코딩 사용
#   - uid=1000, gid=100: 사용자 및 그룹 ID 설정

# ////////////////////////////////////////////////////////////////////////

$ printf "hello" > hello.txt
# hello.txt 파일을 생성하고 "hello"라는 문자열을 입력

$ printf "test" > test.txt
# test.txt 파일을 생성하고 "test"라는 문자열을 입력

$ ls -l
# 현재 디렉토리의 파일 목록과 상세 정보 출력
total 8 # 총 파일의 크기: block 수
-rw-r--r-- 1 devel users 5 Sep 27 01:10 hello.txt  # hello.txt 파일 (크기: 5바이트)
-rw-r--r-- 1 devel users 4 Sep 27 01:11 test.txt   # test.txt 파일 (크기: 4바이트)

$ ln hello.txt helloworld.txt
# hello.txt의 하드 링크(hard link)인 helloworld.txt 생성

$ ln -s test.txt testing
# test.txt의 심볼릭 링크(symbolic link)인 testing 생성

$ ls -l
# 파일 목록 확인
total 12
-rw-r--r-- 2 devel users 5 Sep 27 01:10 hello.txt       # hello.txt (하드 링크 수: 2)
-rw-r--r-- 2 devel users 5 Sep 27 01:10 helloworld.txt  # helloworld.txt (hello.txt의 하드 링크)
lrwxrwxrwx 1 devel users 8 Sep 27 01:12 testing -> test.txt  # 심볼릭 링크 (test.txt를 가리킴)
-rw-r--r-- 1 devel users 4 Sep 27 01:11 test.txt        # test.txt 파일

# hard link count:2가 있는 부분 만큼 total 추가
# l:soft symbolic link flag

# 주요 개념:
# ln <원본 파일> <하드 링크>  -> 같은 inode를 공유 (동일한 파일)
# ln -s <원본 파일> <심볼릭 링크>  -> 원본 파일을 가리키는 별도 파일 (경로 기반)

$ printf ", world!"\\n >> helloworld.txt
# helloworld.txt 파일에 ", world!" 문자열을 추가

$ cat helloworld.txt
# helloworld.txt 파일 내용 출력
hello, world!
$ cat hello.txt
# hello.txt 파일 내용 출력
hello, world!

$ ls -l
total 12
-rw-r--r-- 2 devel users 14 Sep 27 01:12 hello.txt
# 5 -> 14 (5바이트에서 14바이트로 증가) 
-rw-r--r-- 2 devel users 14 Sep 27 01:12 helloworld.txt
lrwxrwxrwx 1 devel users  8 Sep 27 01:12 testing -> test.txt
-rw-r--r-- 1 devel users  4 Sep 27 01:11 test.txt

$ printf ", test, and test!"\\n >> testing 

$ cat test.txt
test, test, and test!
$ cat testing
test, test, and test!

$ ls -l
total 12
-rw-r--r-- 2 devel users 14 Sep 27 01:12 hello.txt
-rw-r--r-- 2 devel users 14 Sep 27 01:12 helloworld.txt
lrwxrwxrwx 1 devel users  8 Sep 27 01:12 testing -> test.txt
# 8 -> 8 유지
-rw-r--r-- 1 devel users 22 Sep 27 01:13 test.txt
# 4 -> 22 (4바이트에서 22바이트로 증가) soft link는 다른 inode를 가지고 있음 따라서 testing의 크기는 변하지 않음

$ rm hello.txt 
# rm: remove hello.txt
# hello.txt 파일 삭제
$ rm test.txt
# broken (soft) link
# test.txt 파일 삭제

$ ls -l
total 4
-rw-r--r-- 1 devel users 14 Sep 27 01:12 helloworld.txt
# 앞에 1 부분은 hard link count
# 2 -> 1 (2개의 하드 링크에서 1개로 감소)
lrwxrwxrwx 1 devel users  8 Sep 27 01:12 testing -> test.txt

$ cat helloworld.txt
hello, world!

$ cat testing
cat: testing: No such file or directory

# ////////////////////////////////////////////////////////////////////////
: '
===== 생성된 파일 목록 =====
total 4
drwxr-xr-x 2 user group  4096 Mar 17 10:00 my_directory
-rw-r--r-- 1 user group    14 Mar 17 10:00 my_file.txt
-rw-r--r-- 1 user group    14 Mar 17 10:00 my_hardlink
lrwxrwxrwx 1 user group     9 Mar 17 10:00 my_symlink -> my_file.txt
prw-r--r-- 1 user group     0 Mar 17 10:00 my_fifo
srwxr-xr-x 1 user group     0 Mar 17 10:00 my_socket

===== 📌 Unix 파일 타입 설명 =====
- d: 디렉토리
- -: 일반 파일 (Regular file)
- l: 심볼릭 링크 (Symbolic link)
- p: FIFO (Named pipe)
- s: 소켓 (Socket)
- c: 문자 디바이스 파일 (Character device file)
- b: 블록 디바이스 파일 (Block device file)
'
# ////////////////////////////////////////////////////////////////////////

#!/bin/bash

# 하드 링크 개수를 확인하는 스크립트
# Unix 파일 시스템에서 디렉토리의 하드 링크 개수를 계산하는 원리를 설명함

# 샘플 디렉토리 및 하위 디렉토리 생성
mkdir -p sample/dir1 sample/dir2

# 디렉토리 리스트 출력
echo "===== 디렉토리 리스트 및 하드 링크 개수 ====="
ls -ld sample sample/dir1 sample/dir2

echo ""
echo "===== 하드 링크 개수 설명 ====="

# 하드 링크 개수 설명 출력
echo "sample 디렉토리:"
echo "1 (자기 자신) + 1 ('.' 현재 디렉토리) + 2 ('..'을 통한 하위 디렉토리 참조) = 4"
echo "dir1, dir2 디렉토리:"
echo "1 (자기 자신) + 1 ('..'을 통한 부모 디렉토리 참조) = 2"

# ////////////////////////////////////////////////////////////////////////

Hidden files
Hidden files start with a “.” in Unix file systems

Special (hidden) entries
“.”	    current directory
“..”	parent directory (hence “cd ..”)

# ////////////////////////////////////////////////////////////////////////
kyoungsoo@user:~$ ls -ld sample
drwxr-xr-x 4 kyoungsoo kyoungsoo 4096 Sep 12 11:55 sample
# sample 디렉토리의 상세 정보를 출력
# drwxr-xr-x: 디렉토리, 소유자 읽기/쓰기/실행, 그룹 읽기/실행, 기타 읽기/실행 권한
# 4: 하드 링크 개수 (자기 자신, '.', '..'을 통한 하위 디렉토리 참조)
# kyoungsoo: 소유자
# kyoungsoo: 그룹
# 4096: 디렉토리 크기 (바이트 단위)
# Sep 12 11:55: 마지막 수정 시간
# sample: 디렉토리 이름

kyoungsoo@user:~$ ls -l sample
total 8
drwxr-xr-x 2 kyoungsoo kyoungsoo 4096 Sep 12 11:55 dir1
drwxr-xr-x 2 kyoungsoo kyoungsoo 4096 Sep 12 11:55 dir2
# sample 디렉토리 내부의 파일 및 디렉토리 목록과 상세 정보를 출력
# total 8: 디렉토리 내의 파일들이 차지하는 총 블록 수
# drwxr-xr-x: 디렉토리, 소유자 읽기/쓰기/실행, 그룹 읽기/실행, 기타 읽기/실행 권한
# 2: 하드 링크 개수 (자기 자신, '..'을 통한 부모 디렉토리 참조)
# kyoungsoo: 소유자
# kyoungsoo: 그룹
# 4096: 디렉토리 크기 (바이트 단위)
# Sep 12 11:55: 마지막 수정 시간
# dir1, dir2: 디렉토리 이름
: '
ls -ld sample 명령어는 sample 디렉토리의 상세 정보를 출력합니다.
ls -l sample 명령어는 sample 디렉토리 내부의 파일 및 디렉토리 목록과 상세 정보를 출력합니다.
'
# ////////////////////////////////////////////////////////////////////////
: '
Filesystem Hierarchy Standard (FHS)
- Defines the directory structure and directory contents in Unix-like operating systems
'
$ ls -l /
total 76
drwxr-xr-x   2 root root  4096 Sep  3 02:11 bin
: '
d: 디렉토리임을 나타냅니다.
rwxr-xr-x: 파일 권한을 나타냅니다.
rwx: 소유자(root)의 권한 (읽기, 쓰기, 실행)
r-x: 그룹(root)의 권한 (읽기, 실행)
r-x: 기타 사용자의 권한 (읽기, 실행)
2: 하드 링크의 개수를 나타냅니다.
root: 파일 소유자의 이름을 나타냅니다.
root: 파일 소유자 그룹의 이름을 나타냅니다.
4096: 디렉토리의 크기를 바이트 단위로 나타냅니다.
Sep  3 02:11: 마지막 수정 시간을 나타냅니다.
bin: 디렉토리의 이름을 나타냅니다.
'
drwxr-xr-x   2 root root  4096 Sep  3 02:11 bin
# bin 디렉토리
# drwxr-xr-x: 디렉토리, 소유자 읽기/쓰기/실행, 그룹 읽기/실행, 기타 읽기/실행 권한
# 2: 하드 링크 개수
# root: 소유자
# root: 그룹
# 4096: 디렉토리 크기 (바이트 단위)
# Sep  3 02:11: 마지막 수정 시간

drwxr-xr-x   3 root root  4096 Aug  1 20:37 boot
# boot 디렉토리
drwxr-xr-x  20 root root  4020 Sep  1 23:17 dev
# dev 디렉토리
drwxr-xr-x  88 root root  4096 Sep  3 11:59 etc
# etc 디렉토리
drwxr-xr-x   5 root root  4096 Mar 24  2022 home
# home 디렉토리
drwxr-xr-x  13 root root  4096 Jul  5 21:40 lib
# lib 디렉토리
drwxr-xr-x   7 root root  4096 Sep  3 02:11 lib64
# lib64 디렉토리
drwx------   2 root root 16384 Mar 23  2022 lost+found
# lost+found 디렉토리
drwxr-xr-x   2 root root  4096 Mar 21  2022 media
# media 디렉토리
drwxr-xr-x   4 root root  4096 Sep 16  2022 mnt
# mnt 디렉토리
drwxr-xr-x  16 root root  4096 Jul 16 19:05 opt
# opt 디렉토리
dr-xr-xr-x 447 root root     0 Aug 19 21:52 proc
# proc 디렉토리
drwx------   7 root root  4096 Sep  3 11:59 root
# root 디렉토리
drwxr-xr-x  19 root root   740 Sep  1 23:16 run
# run 디렉토리
drwxr-xr-x   2 root root 12288 Sep  3 02:11 sbin
# sbin 디렉토리
dr-xr-xr-x  12 root root     0 Aug 19 21:52 sys
# sys 디렉토리
drwxrwxrwt  17 root root  1100 Sep  3 18:51 tmp
# tmp 디렉토리
drwxr-xr-x  12 root root  4096 Sep 20  2022 usr
# usr 디렉토리
drwxr-xr-x  10 root root  4096 Sep  3 01:37 var
# var 디렉토리
: ' root == / (root directory)
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── lib64
├── lost+found
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── sys
├── tmp
├── usr
└── var

https://refspecs.linuxfoundation.org/fhs.shtml
Directory Description mantained by Linux Foundation
'
# ////////////////////////////////////////////////////////////////////////

# Filesystem & Security
: '
Standard *nix Access Control Listss(ACL)
- three levels of access
    + owner, group, other
- three kindss of permissions
    + read(r), write(w), execute(x)

drwxrw-rwx
d: directory
rwx: owner (read, write, execute)
rw-: group  (read, write)
rwx: other 
'
# ////////////////////////////////////////////////////////////////////////

# modify with chmod command
devel@csapvm ~/temp $ echo "hello" > test.txt
# test.txt 파일을 생성하고 "hello"라는 문자열을 입력
devel@csapvm ~/temp $ ls -l
# 현재 디렉토리의 파일 목록과 상세 정보 출력
-rw-r--r-- 1 devel devel 6 Sep 16 19:37 test.txt
# test.txt 파일의 권한: 소유자 읽기/쓰기, 그룹 읽기, 기타 읽기

devel@csapvm ~/temp $ chmod g+w test.txt
# test.txt 파일에 그룹 쓰기 권한 추가
devel@csapvm ~/temp $ ls -l
# 현재 디렉토리의 파일 목록과 상세 정보 출력
-rw-rw-r-- 1 devel devel 6 Sep 16 19:37 test.txt
# test.txt 파일의 권한: 소유자 읽기/쓰기, 그룹 읽기/쓰기, 기타 읽기

devel@csapvm ~/temp $ echo "ls -l" > script.sh
# script.sh 파일을 생성하고 "ls -l" 명령어를 입력
devel@csapvm ~/temp $ ./script.sh
# script.sh 파일을 실행하려고 시도
-bash: ./script.sh: Permission denied
# 실행 권한이 없어서 실행 실패
devel@csapvm ~/temp $ ls -l
# 현재 디렉토리의 파일 목록과 상세 정보 출력
-rw-r--r-- 1 devel devel 6 Sep 16 19:38 script.sh
# script.sh 파일의 권한: 소유자 읽기/쓰기, 그룹 읽기, 기타 읽기

devel@csapvm ~/temp $ chmod 750 script.sh
# 3 bit로 보면 7 / 5 / 0 > 111 / 101 / 000 > 이대로 권한 허용해주기임
# script.sh 파일에 소유자 읽기/쓰기/실행, 그룹 읽기/실행, 기타 권한 없음으로 변경
devel@csapvm ~/temp $ ls -l
# 현재 디렉토리의 파일 목록과 상세 정보 출력
-rwxr-x--- 1 devel devel 6 Sep 16 19:38 script.sh
# script.sh 파일의 권한: 소유자 읽기/쓰기/실행, 그룹 읽기/실행, 기타 권한없음

# ////////////////////////////////////////////////////////////////////////

# Sticky bit

devel@csapvm $ ls -ld /tmp
drwxrwxrwt 6 root root 240 Oct  8 14:32 /tmp

# /tmp 디렉토리의 권한: 소유자 읽기/쓰기/실행, 그룹 읽기/쓰기/실행, 기타 읽기/쓰기/실행
# t: sticky bit (다른 사용자가 파일을 삭제, 이름 변경 할 수 없음)
# flag available in struct stat(S_ISVTX)
# - man 2 stat
# - man 7 inode

# S_ISVTX 플래그는 struct stat에서 사용 가능하며, sticky bit가 설정된 파일이나 디렉토리를 나타냅니다.
# man 2 stat: stat 시스템 호출에 대한 매뉴얼 페이지를 참조합니다. 파일의 상태를 가져오는 시스템 호출
# man 7 inode: inode에 대한 매뉴얼 페이지를 참조합니다. 파일의 메타데이터를 저장하는 데이터 구조

# ////////////////////////////////////////////////////////////////////////

# World-writable directory with execute permission

devel@csapvm $ ls -ld /tmp
drwxrwxrwx 6 root root 240 Oct  8 14:32 /tmp
or
drwxrwxrwt 6 root root 240 Oct  8 14:32 /tmp

: '
world-writable directories on a file system with execute permission are a security risk
anyone with access to the system may place an executable and run it
권한 있는 누구나 사용 가능
(typical scenario: webserver breach > write script to /tmp > execute it)

world-writable flag in struct stat (S_IWOTH)
filesystem may disallow execution: use fstatfs() and check for ST_NOEXEC flag'

# ////////////////////////////////////////////////////////////////////////
# Check SUID/SGID bits
ls -l /usr/bin/sudo
# Output: -rwsr-xr-x 1 root root 204320 Sep 1 16:17 /usr/bin/sudo

# Check filesystem flags
fstatfs /path/to/check
# Check for ST_NOSUID flag
# binary executable with permissions of owner(root in this case)
# - useful to give temporary permissions to owner
# - trusted binary owned by rrot must have suid/sgid bits set
: '
SUID (Set User ID): 파일을 실행하는 사용자가 파일 소유자의 권한으로 실행되도록 설정하는 비트.
SGID (Set Group ID): 파일을 실행하는 사용자가 파일 소유 그룹의 권한으로 실행되도록 설정하는 비트.
Sticky Bit: 디렉토리의 경우, 파일 소유자만 해당 파일을 삭제할 수 있도록 설정하는 비트.

STAT(S_ISUID/S_ISGID): man 2 stat, man 7 inode
filesystem may disallow SUID
fstatfs(): check for ST_NOEXEC flag

ST_NOEXEC는 파일 시스템에서 실행 권한을 제한하는 플래그입니다. 
이 플래그가 설정된 파일 시스템에서는 실행 파일을 실행할 수 없습니다. 
이는 보안상의 이유로 특정 파일 시스템에서 실행 파일의 실행을 방지하기 위해 사용됩니다.
'
# ////////////////////////////////////////////////////////////////////////

# page 36
# POSIX ACLs are limited to acces permissions for user,group and everybody else
# Extended file attributes(xattrs) provide 
# an extensivle and more flexible way to store metadata
: '
확장 파일 속성(xattrs):

setfacl/getfacl 명령어를 사용하여 특정 사용자에 대한 ACL 설정/가져오기.
namespace.attribute 형식의 key=value 쌍으로 저장.
네임스페이스: security, system, trusted, user.
'
# ////////////////////////////////////////////////////////////////////////
# Extended File ACL

# Check whether a filesystem supports xattrs
devel@csapvm $ mount | grep "/" 
# Check mounted filesystems and their options
/dev/sda4 on / type ext4 (rw,noatime)

devel@csapvm $ cat /proc/fs/ext4/sda4/options | grep xattr
# Check if the filesystem supports extended attributes
user_xattr

# Extended ACL: set/get ACLs with setfacl/getfacl
devel@csapvm $ echo "Hello" > file.txt
# Create file.txt and write "Hello" into it

devel@csapvm $ chmod 640 file.txt
# Change the permissions of file.txt to 640 (rw-r-----)

devel@csapvm $ ls -l file.txt
# List file.txt with detailed information
-rw-r----- 1 devel devel 6 Mar  7 19:75 file.txt

devel@csapvm $ setfacl -m u:svn:r file.txt
# Set an ACL to give user 'svn' read permission on file.txt

devel@csapvm $ ls -l file.txt
# List file.txt with detailed information (note the '+' indicating ACLs)
-rw-r-----+ 1 devel devel 6 Mar  7 19:75 file.txt

devel@csapvm $ getfacl file.txt
# Get the ACLs of file.txt
# file: file.txt
# owner: devel
# group: devel
user::rw-
user:svn:r--
group::---
mask::r--
other::---

# ////////////////////////////////////////////////////////////////////////

# Extended File System Attributes: User

# Set/get arbitrary attributes with setfattr/getfattr
devel@csapvm $ md5sum file.txt
# Calculate the MD5 checksum of file.txt
09f7e02f1290be211da707a266f153b3  file.txt

devel@csapvm $ setfattr -n user.checksum.md5 -v 09f7e02f1290be211da707a266f153b3 file.txt
# Set the extended attribute 'user.checksum.md5' with the value '09f7e02f1290be211da707a266f153b3' on file.txt

devel@csapvm $ ls -l
# List files with detailed information
total 8
-rw-r--r-- 1 devel devel 6 Mar  7 19:75 file.txt

devel@csapvm $ getfattr file.txt
# Get all extended attributes of file.txt
# file: file.txt
user.checksum.md5

devel@csapvm $ getfattr -n user.checksum.md5 file.txt
# Get the value of the extended attribute 'user.checksum.md5' of file.txt
# file: file.txt
user.checksum.md5="09f7e02f1290be211da707a266f153b3"

devel@csapvm $ setfattr -x user.checksum.md5 file.txt
# Remove the extended attribute 'user.checksum.md5' from file.txt

devel@csapvm $ getfattr file.txt
# Get all extended attributes of file.txt (should be none)
# file: file.txt

devel@csapvm $ getfattr -n user.checksum.md5 file.txt
# Try to get the value of the extended attribute 'user.checksum.md5' of file.txt (should not exist)
# file: file.txt: user.checksum.md5: No such attribute



