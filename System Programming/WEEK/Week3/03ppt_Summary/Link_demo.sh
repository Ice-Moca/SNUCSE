#!/bin/bash

# 🔹 Step 1: 원본 파일 생성
echo "Hello, this is a sample file." > original.txt

# 🔹 Step 2: 하드 링크 생성
ln original.txt hardlink.txt

# 🔹 Step 3: 심볼릭 링크 생성
ln -s original.txt symlink.txt

# 🔹 Step 4: 파일 리스트 출력 (inode 정보 확인)
echo "===== 파일 리스트 (inode 포함) ====="
ls -li original.txt hardlink.txt symlink.txt

# 🔹 Step 5: 원본 파일 삭제 후 상태 확인
rm original.txt
echo "===== 원본 파일 삭제 후 상태 ====="
ls -li hardlink.txt symlink.txt || echo "심볼릭 링크가 깨졌습니다!"

# 🔹 Step 6: 파일 내용 확인
echo "===== 하드 링크 내용 확인 ====="
cat hardlink.txt
echo "===== 심볼릭 링크 내용 확인 ====="
cat symlink.txt || echo "심볼릭 링크가 깨졌습니다!"

# 🔹 정리된 개념 (echo를 사용해 출력)
echo ""
echo "===== 📌 하드 링크 vs 심볼릭 링크 비교 ====="
echo "1️⃣ 하드 링크 (hardlink.txt):"
echo "   ✅ 원본 파일과 같은 inode 공유 (같은 파일로 간주)"
echo "   ✅ 원본 파일 삭제 후에도 데이터 유지"
echo ""
echo "2️⃣ 심볼릭 링크 (symlink.txt):"
echo "   ❌ 원본 파일을 가리키는 별도 파일 (다른 inode)"
echo "   ❌ 원본 파일 삭제 시 링크가 깨짐 (Broken Link)"
echo ""
