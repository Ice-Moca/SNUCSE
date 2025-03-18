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

////////////////////////////////////////////////////////////////////////

devel@caspvm $ mount
# 현재 시스템에 마운트된 파일 시스템 목록을 확인하는 명령어

/dev/sda4 on / type ext4 (rw,noatime)
# /dev/sda4 장치를 루트 파일 시스템 (/)로 마운트
# 파일 시스템 타입: ext4
# 옵션:
#   - rw: 읽기/쓰기 허용
#   - noatime: 파일 접근 시간(atime) 업데이트 방지 (성능 최적화)

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

////////////////////////////////////////////////////////////////////////

$ printf "hello" > hello.txt
# hello.txt 파일을 생성하고 "hello"라는 문자열을 입력

$ printf "test" > test.txt
# test.txt 파일을 생성하고 "test"라는 문자열을 입력

$ ls -l
# 현재 디렉토리의 파일 목록과 상세 정보 출력
total 8
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

# 주요 개념:
# ln <원본 파일> <하드 링크>  -> 같은 inode를 공유 (동일한 파일)
# ln -s <원본 파일> <심볼릭 링크>  -> 원본 파일을 가리키는 별도 파일 (경로 기반)

////////////////////////////////////////////////////////////////////////

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

////////////////////////////////////////////////////////////////////////

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

////////////////////////////////////////////////////////////////////////

#page 20