#!/bin/bash

# Loop through test files from test0.c to test5.c
for i in {0..5}
do
  # Run the reference decomment program and save output and error to files
  ./reference/sampledecomment < ./test_files/test${i}.c > ./output/reference_output${i}.txt 2> ./output/reference_error${i}.txt

  # Run the student's decomment program and save output and error to files
  ./src/decomment < ./test_files/test${i}.c > ./output/student_output${i}.txt 2> ./output/student_error${i}.txt

  # Compare the outputs
  diff ./output/reference_output${i}.txt ./output/student_output${i}.txt > ./output/diff_output${i}.txt
  diff ./output/reference_error${i}.txt ./output/student_error${i}.txt > ./output/diff_error${i}.txt
done