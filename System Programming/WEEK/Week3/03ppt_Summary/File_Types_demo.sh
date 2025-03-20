#!/bin/bash

# 데모를 위한 디렉토리 생성
mkdir -p /tmp/demo
cd /tmp/demo || exit

# 1️⃣ 디렉토리 생성
mkdir my_directory

# 2️⃣ 일반 파일 생성
echo "Hello, Unix!" > my_file.txt

# 3️⃣ 하드 링크 생성
ln my_file.txt my_hardlink

# 4️⃣ 심볼릭 링크 생성
ln -s my_file.txt my_symlink

# 5️⃣ FIFO(named pipe) 생성
mkfifo my_fifo

# 6️⃣ 소켓 생성
socket_name="my_socket"
rm -f $socket_name
mknod $socket_name s

# 7️⃣ 파일 타입 확인
echo "===== 생성된 파일 목록 ====="
ls -l

# 8️⃣ 정리된 개념 출력
echo ""
echo "===== 📌 Unix 파일 타입 설명 ====="
echo "- d: 디렉토리"
echo "- -: 일반 파일 (Regular file)"
echo "- l: 심볼릭 링크 (Symbolic link)"
echo "- p: FIFO (Named pipe)"
echo "- s: 소켓 (Socket)"
echo "- c: 문자 디바이스 파일 (Character device file)"
echo "- b: 블록 디바이스 파일 (Block device file)"

