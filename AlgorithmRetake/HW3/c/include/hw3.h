#ifndef HW3_H
#define HW3_H

/**
 * @brief Represents a blocked cell (hole) on the board.
 */
typedef struct {
    int row;
    int col;
} Hole;

long long solve_iterative_nqueens(int n, const Hole *holes, int h);
long long solve_recursive_nqueens(int n, const Hole *holes, int h);

#endif  // HW3_H
