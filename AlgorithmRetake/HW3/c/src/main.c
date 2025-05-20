#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "hw3.h"

int main() {
    int n, h;
    if (scanf("%d %d", &n, &h) != 2) {
        fprintf(stderr, "Usage: <board size> <hole count>\n");
        return EXIT_FAILURE;
    }

    Hole holes[3];
    for (int i = 0; i < h; ++i) {
        if (scanf("%d %d", &holes[i].row, &holes[i].col) != 2) {
            fprintf(stderr, "Error reading hole %d\n", i);
            return EXIT_FAILURE;
        }
    }

    // iterative backtracking
    clock_t start_iter = clock();
    long long count_iter = solve_iterative_nqueens(n, holes, h);
    clock_t end_iter = clock();
    double time_iter = (double)(end_iter - start_iter) / CLOCKS_PER_SEC * 1000.0;

    // recursive backtracking
    clock_t start_rec = clock();
    long long count_rec = solve_recursive_nqueens(n, holes, h);
    clock_t end_rec = clock();
    double time_rec = (double)(end_rec - start_rec) / CLOCKS_PER_SEC * 1000.0;

    printf("Iterative: %lld\n", count_iter);
    printf("Elapsed Time (ms): %.6f\n", time_iter);
    printf("Recursive: %lld\n", count_rec);
    printf("Elapsed Time (ms): %.6f\n", time_rec);

    return 0;
}
