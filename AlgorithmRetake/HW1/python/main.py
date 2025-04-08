import sys
import time
from src.hw1 import randomized_select, deterministic_select, check_selection

def main():
    data = sys.stdin.read().split()
    if len(data) < 2:
        return
    n = int(data[0])
    i = int(data[1])
    if len(data) < 2 + n:
        return
    original = list(map(int, data[2:2+n]))
    arr_rand = original.copy()
    arr_det = original.copy()
    
    start_time = time.time()
    result_rand = randomized_select(arr_rand, 0, n-1, i)
    elapsed_rand = (time.time() - start_time) * 1000.0
    check_rand = check_selection(original, i, result_rand)
    
    start_time = time.time()
    result_det = deterministic_select(arr_det, 0, n-1, i)
    elapsed_det = (time.time() - start_time) * 1000.0
    check_det = check_selection(original, i, result_det)
    
    print("Randomized: " + ("correct" if check_rand else "incorrect"))
    print("Elapsed Time: {:.6f}".format(elapsed_rand))
    print("Deterministic: " + ("correct" if check_det else "incorrect"))
    print("Elapsed Time: {:.6f}".format(elapsed_det))

if __name__ == "__main__":
    main()
