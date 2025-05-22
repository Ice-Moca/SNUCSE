from typing import List, Tuple

def solve_iterative_nqueens(n: int, holes: List[tuple]) -> int:
    """
    Solves the n-queens problem using iterative backtracking.

    Parameters:
        board_size (int): Size of the board. (Number of queens)
        blocked_positions (List[tuple]): List of (row, col) tuples representing blocked positions.

    Returns:
        int: Count of valid solutions.
    """
    # Step 1: Initialize hole board
    hole_board = []
    for _ in range(n):        
        row = []
        for _ in range(n):      
            row.append(False)
        hole_board.append(row) 
    # Step 2: Fill the hole as True
    for row, col in holes:
        if 0 <= row < n and 0 <= col < n:
            hole_board[row][col] = True

    # Step 3: Build dicoinary of columns that has 0 to n-1 as key and the values are empty lists
    column_to_holes = {}
    for col in range(n):
        column_to_holes[col] = []
    # Fill the row index of the holes in the matched column
    for row, col in holes:
        if 0 <= row < n and 0 <= col < n:
            column_to_holes[col].append(row)

    # Step 4: Create segments for each column
    # Segments are build to make a list that has no holes in between
    # The segments are tuples of (col, row_start, row_end)
    # col: column index of the orignal board
    segments: List[Tuple[int,int,int]] = []
    for col in range(n):
        blocked_rows = sorted(column_to_holes[col])
        start_row = 0
        # Check if there are any blocked rows in the column
        # If there are, create segments
        for blocked_row in blocked_rows:
            if start_row <= blocked_row - 1:
                segments.append((col, start_row, blocked_row - 1))
            start_row = blocked_row + 1
        # Check if there are any possible rowws left behind the holes
        # If there are, create segments
        if start_row <= n - 1:
            segments.append((col, start_row, n - 1))
    total_segments = len(segments)

    # Step 5: Helper functions for checking holes between two points
    def is_hole_between_in_row(row: int, col1: int, col2: int) -> bool:
        # Check the left and right columns
        if col1 < col2:
            left, right = col1, col2
        else:
            left, right = col2, col1
        # Check if there is a hole between col1 and col2 in the same row
        for c in range(left + 1, right):
            if hole_board[row][c]:
                return True
        return False

    def is_hole_between_in_col(col: int, row1: int, row2: int) -> bool:
        # Check the top and bottom rows
        if row1 < row2:
            top, bottom = row1, row2
        else:
            top, bottom = row2, row1
        # Check if there is a hole between row1 and row2 in the same column
        for r in range(top + 1, bottom):
            if hole_board[r][col]:
                return True
        return False

    def is_hole_between_in_diag(r1: int, c1: int, r2: int, c2: int) -> bool:
        # Check the diagonal direction
        if r1 < r2:
            row_direction = 1
        else:
            row_direction = -1
        if c1 < c2:
            col_direction = 1
        else:
            col_direction = -1
        # Check if there is a hole between (r1, c1) and (r2, c2) in the diagonal
        row, col = r1 + row_direction, c1 + col_direction
        while row != r2 and col != c2:
            if hole_board[row][col]:
                return True
            row += row_direction
            col += col_direction
        return False

    # Step 6: Initialize variables
    # Positions of queens per depth
    queen_rows = [0]*n
    queen_cols = [0]*n
    # Count of solutions
    solution_count = 0

    # Step 7: Iterative backtracking using stack
    # Stack Frame: [segment_index, placed_queens_count, part, next_row_to_try]
    stack: List[List[int]] = [[0, 0, 0, 0]]
    while stack:
        frame = stack[-1]
        segment_index, placed_count, part, next_row = frame

        # All queens placed: count a solution
        if placed_count == n:
            solution_count += 1
            # Exit the current stack
            stack.pop()
            continue

        # Out of segments or not enough segments left: break
        # Do not go deeper, some kind of pruning added for performance
        if segment_index == total_segments or total_segments - segment_index < n - placed_count:
            stack.pop()
            continue
        
        # Part 1: skip current segment
        if part == 0:
            # change to Part 2
            frame[2] = 1  
            stack.append([segment_index + 1, placed_count, 0, 0])
            continue
        
        # Part 2-1: initialize row scanning for placement
        if part == 1:
            col, row_start, row_end = segments[segment_index]
            # Set the next row to try search for queen placement to row_start
            frame[3] = row_start
            # change part not to go back to Part 1 or 2-1
            frame[2] = 2

        # Part 2-2: scan rows in the segment to place queen
        col, row_start, row_end = segments[segment_index]
        placed = False
        while frame[3] <= row_end:
            # Get the current row to try
            row = frame[3]
            # Increse the row to try for the next iteration
            frame[3] += 1
            # Check if the current position is blocked by a hole
            if hole_board[row][col]:
                continue
            
            # Check if the current position is safe to place a queen
            safe = True
            for i in range(placed_count):
                qr, qc = queen_rows[i], queen_cols[i]
                # Check if the current position is blocked by a hole or attaked by another queen
                if qr == row and not is_hole_between_in_row(row, qc, col):
                    safe = False
                    break
                if qc == col and not is_hole_between_in_col(col, qr, row):
                    safe = False
                    break
                if abs(qr - row) == abs(qc - col) and not is_hole_between_in_diag(qr, qc, row, col):
                    safe = False
                    break
            if not safe:
                continue
        
            # Place the queen at (r, col)
            queen_rows[placed_count] = row
            queen_cols[placed_count] = col
            # Update the stack frame to reflect the placement
            stack.append([segment_index + 1, placed_count + 1, 0, 0])
            placed = True
            break
        
        # If no queen was placed in the current segment, pop the stack
        if not placed:
            stack.pop()

    return solution_count


def solve_recursive_nqueens(n: int, holes: List[tuple]) -> int:
    """
    Solves the n-queens problem using recursive backtracking.

    Parameters:
        n (int): Size of the board. (Number of queens)
        holes (List[tuple]): List of (row, col) tuples representing blocked positions.

    Returns:
        int: Count of valid solutions.
    """
    # Step 1: Initialize hole board
    hole_board = []
    for _ in range(n):        
        row = []
        for _ in range(n):      
            row.append(False)
        hole_board.append(row) 
    # Step 2: Fill the hole as True
    for row, col in holes:
        if 0 <= row < n and 0 <= col < n:
            hole_board[row][col] = True

    # Step 3: Build dicoinary of columns that has 0 to n-1 as key and the values are empty lists
    column_to_holes = {}
    for col in range(n):
        column_to_holes[col] = []
    # Fill the row index of the holes in the matched column
    for row, col in holes:
        if 0 <= row < n and 0 <= col < n:
            column_to_holes[col].append(row)

    # Step 4: Create segments for each column
    # Segments are build to make a list that has no holes in between
    # The segments are tuples of (col, row_start, row_end)
    # col: column index of the orignal board
    segments: List[Tuple[int,int,int]] = []
    for col in range(n):
        blocked_rows = sorted(column_to_holes[col])
        start_row = 0
        # Check if there are any blocked rows in the column
        # If there are, create segments
        for blocked_row in blocked_rows:
            if start_row <= blocked_row - 1:
                segments.append((col, start_row, blocked_row - 1))
            start_row = blocked_row + 1
        # Check if there are any possible rowws left behind the holes
        # If there are, create segments
        if start_row <= n - 1:
            segments.append((col, start_row, n - 1))
    total_segments = len(segments)

    # Step 5: Helper functions for checking holes between two points
    def is_hole_between_in_row(row: int, col1: int, col2: int) -> bool:
        # Check the left and right columns
        if col1 < col2:
            left, right = col1, col2
        else:
            left, right = col2, col1
        # Check if there is a hole between col1 and col2 in the same row
        for c in range(left + 1, right):
            if hole_board[row][c]:
                return True
        return False

    def is_hole_between_in_col(col: int, row1: int, row2: int) -> bool:
        # Check the top and bottom rows
        if row1 < row2:
            top, bottom = row1, row2
        else:
            top, bottom = row2, row1
        # Check if there is a hole between row1 and row2 in the same column
        for r in range(top + 1, bottom):
            if hole_board[r][col]:
                return True
        return False

    def is_hole_between_in_diag(r1: int, c1: int, r2: int, c2: int) -> bool:
        # Check the diagonal direction
        if r1 < r2:
            row_direction = 1
        else:
            row_direction = -1
        if c1 < c2:
            col_direction = 1
        else:
            col_direction = -1
        # Check if there is a hole between (r1, c1) and (r2, c2) in the diagonal
        row, col = r1 + row_direction, c1 + col_direction
        while row != r2 and col != c2:
            if hole_board[row][col]:
                return True
            row += row_direction
            col += col_direction
        return False

    # Step 6: Initialize variables
    # Positions of queens per depth
    queen_rows = [0]*n
    queen_cols = [0]*n
    # Count of solutions
    solution_count = 0

    # Step 7: Recursive backtracking
    # Backtracking function
    def backtrack(seg_idx: int, placed: int):
        """
        Recursive backtracking function to place queens.

        Args:
            seg_idx (int): Segment index to consider for placement.
            placed (int): Number of queens already placed.
        """
        nonlocal solution_count
        # All queens placed: count a solution
        if placed == n:
            solution_count += 1
            return
        # Out of segments or not enough segments left: break
        # Do not go deeper, some kind of pruning added for performance
        if seg_idx == total_segments or total_segments - seg_idx < n - placed:
            return

        # Part 1: Skip segment
        backtrack(seg_idx + 1, placed)

        # Part 2: Try placing queen in segment
        col, row_start, row_end = segments[seg_idx]
        for row in range(row_start, row_end + 1):
            # Check if the current position is blocked by a hole
            if hole_board[row][col]:
                continue
            safe = True
            for i in range(placed):
                # Check if the current position is blocked by a hole or attacked by another queen
                qr, qc = queen_rows[i], queen_cols[i]
                if qr == row and not is_hole_between_in_row(row, qc, col):
                    safe = False
                    break
                if qc == col and not is_hole_between_in_col(col, qr, row):
                    safe = False
                    break
                if abs(qr - row) == abs(qc - col) and not is_hole_between_in_diag(qr, qc, row, col):
                    safe = False
                    break
            if not safe:
                continue
            # Place the queen at (row, col)
            queen_rows[placed] = row
            queen_cols[placed] = col
            backtrack(seg_idx + 1, placed + 1)

    backtrack(0, 0)
    return solution_count
