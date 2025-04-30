# Compiler and options
CC = gcc800
CFLAGS = -std=gnu99
TIMEFLAGS = -O3 -D NDEBUG

# Directory paths
REFERENCE_DIR = reference
SRC_DIR = src
TEST_DIR = test

# File definitions
TEST = $(TEST_DIR)/testheapmgr.c
CHUNK_BASE = $(REFERENCE_DIR)/chunkbase.c
CHUNK_BASE_H = $(REFERENCE_DIR)/chunkbase.h
HEAPMGR_H = $(REFERENCE_DIR)/heapmgr.h
HEAPMGR_GNU = $(REFERENCE_DIR)/heapmgrgnu.c
HEAPMGR_KR = $(REFERENCE_DIR)/heapmgrkr.c
HEAPMGR_BASE = $(REFERENCE_DIR)/heapmgrbase.c
HEAPMGR1 = $(SRC_DIR)/heapmgr1.c
HEAPMGR2 = $(SRC_DIR)/heapmgr2.c
CHUNK = $(SRC_DIR)/chunk.c
CHUNK_H = $(SRC_DIR)/chunk.h

# Default target: build all performance test binaries
all: time2all

# Test builds
test1:
	$(CC) $(CFLAGS) $(TEST) $(HEAPMGR1) $(CHUNK) -o $(TEST_DIR)/testheapmgr1

test2:
	$(CC) $(CFLAGS) $(TEST) $(HEAPMGR2) $(CHUNK) -o $(TEST_DIR)/testheapmgr2

testall: test1 test2

# Performance test builds
timegnu:
	$(CC) $(TIMEFLAGS) $(CFLAGS) $(TEST) $(HEAPMGR_GNU) -o $(TEST_DIR)/testheapmgrgnu

timekr:
	$(CC) $(TIMEFLAGS) $(CFLAGS) $(TEST) $(HEAPMGR_KR) -o $(TEST_DIR)/testheapmgrkr

timebase:
	$(CC) $(TIMEFLAGS) $(CFLAGS) $(TEST) $(HEAPMGR_BASE) $(CHUNK_BASE) -o $(TEST_DIR)/testheapmgrbase

time1:
	$(CC) $(TIMEFLAGS) $(CFLAGS) $(TEST) $(HEAPMGR1) $(CHUNK) -o $(TEST_DIR)/testheapmgr1

time2:
	$(CC) $(TIMEFLAGS) $(CFLAGS) $(TEST) $(HEAPMGR2) $(CHUNK) -o $(TEST_DIR)/testheapmgr2

time1all: timegnu timekr timebase time1

time2all: timegnu timekr timebase time1 time2

# Clean
clean:
	rm -f $(TEST_DIR)/testheapmgrgnu $(TEST_DIR)/testheapmgrkr $(TEST_DIR)/testheapmgrbase $(TEST_DIR)/testheapmgr1 $(TEST_DIR)/testheapmgr2
