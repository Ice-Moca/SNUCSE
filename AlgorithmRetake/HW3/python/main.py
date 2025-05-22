import sys
import time
from src.hw3 import solve_iterative_nqueens, solve_recursive_nqueens

def main():
    n, h = map(int, sys.stdin.readline().split())
    holes = [tuple(map(int, sys.stdin.readline().split())) for _ in range(h)]

    # iterative backtracking
    start_iter = time.perf_counter()
    count_iter = solve_iterative_nqueens(n, holes)
    time_iter = (time.perf_counter() - start_iter) * 1000

    # recursive backtracking
    start_rec = time.perf_counter()
    count_rec = solve_recursive_nqueens(n, holes)
    time_rec = (time.perf_counter() - start_rec) * 1000

    print(f"Iterative: {count_iter}")
    print(f"Elapsed Time (ms): {time_iter:.6f}")
    print(f"Recursive: {count_rec}")
    print(f"Elapsed Time (ms): {time_rec:.6f}")

if __name__ == "__main__":
    main()
