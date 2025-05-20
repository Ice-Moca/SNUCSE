from typing import List, Tuple

def solve_iterative_nqueens(n: int, holes: List[tuple]) -> int:
    """
    Solves the n-queens problem using iterative backtracking.

    Parameters:
        n (int): Size of the board. (Number of queens)
        holes (List[tuple]): List of (row, col) tuples representing blocked positions.

    Returns:
        int: Count of valid solutions.
    """
    # TODO
    """
    Iterative backtracking without a separate 'cells' list.
    Board marking approach:
      board[r][c] == 0   : hole
      board[r][c] is None: empty
      board[r][c] == 1   : queen
      board[r][c] >  1   : attack-mark (depth+1)
    """
    # 1) 보드 초기화
    board: List[List[int]] = [[None] * n for _ in range(n)]
    for r, c in holes:
        board[r][c] = 0

    # 2) 앞으로만 표시할 4방향 (뒤쪽은 탐색 안 하므로 생략)
    directions = [(1,0), (0,1), (1,1), (1,-1)]

    # 3) 스택 변수들
    positions: List[int] = [0] * n          # 각 depth에서 놓은 칸의 선형 인덱스
    marked_cells: List[List[Tuple[int,int]]] = [None] * n
    start_idx: List[int] = [0] * (n + 1)    # 각 depth에서 다음 후보를 찾을 선형 인덱스
    depth = 0
    count = 0

    # 4) 백트래킹 루프
    while True:
        # (1) n개 다 놓았으면 해 하나 발견
        if depth == n:
            count += 1
            # backtrack
            depth -= 1
            # undo the queen + its marks
            idx = positions[depth]
            r, c = divmod(idx, n)
            board[r][c] = None
            for rr, cc in marked_cells[depth]:
                board[rr][cc] = None
            # 다음 후보
            start_idx[depth] = idx + 1
            continue

        # (2) depth 레벨에서 start_idx[depth] 이후 후보 탐색
        found = False
        for idx in range(start_idx[depth], n*n):
            r, c = divmod(idx, n)
            if board[r][c] is not None:
                continue  # 구멍, 퀸, 공격 표시 건너뛰기

            # 놓기
            board[r][c] = 1
            mark_val = depth + 2
            marks: List[Tuple[int,int]] = []
            for dr, dc in directions:
                rr, cc = r, c
                while True:
                    rr += dr; cc += dc
                    if not (0 <= rr < n and 0 <= cc < n):
                        break
                    if board[rr][cc] == 0:
                        break  # 구멍 만나면 중단
                    if board[rr][cc] is None:
                        board[rr][cc] = mark_val
                        marks.append((rr, cc))

            # 상태 저장하고 다음 depth
            positions[depth] = idx
            marked_cells[depth] = marks
            start_idx[depth+1] = idx + 1
            # reset this depth의 start (backtrack 후 재사용 위해)
            start_idx[depth] = 0

            depth += 1
            found = True
            break

        # (3) 후보 못 찾았으면 backtrack
        if not found:
            # 더 이상 돌릴 depth 없으면 종료
            if depth == 0:
                break
            depth -= 1
            idx = positions[depth]
            r, c = divmod(idx, n)
            board[r][c] = None
            for rr, cc in marked_cells[depth]:
                board[rr][cc] = None
            start_idx[depth] = idx + 1

    return count

def solve_recursive_nqueens(n: int, holes: List[tuple]) -> int:
    """
    Solves the n-queens problem using recursive backtracking.
    
    Parameters:
        n (int): Size of the board. (Number of queens)
        holes (List[tuple]): List of (row, col) tuples representing blocked positions.

    Returns:
        int: Count of valid solutions.
    """
    # TODO
    """
    구멍이 있는 n x n 보드에서 백트래킹으로 n-queens 해의 개수를 센다.
    board[r][c] == 0  : hole
    board[r][c] is None : 아직 비어 있는 칸
    board[r][c] == 1  : Queen
    board[r][c] == k+1: k번째 Queen이 공격할 수 있는 칸(표시용)
    """
    # 1) 보드 초기화
    board: List[List[int]] = [[None]*n for _ in range(n)]
    for r, c in holes:
        board[r][c] = 0

    # 2) 앞으로만 표시할 4개 방향 (뒤쪽 방향은 탐색 대상이 아니므로 생략)s
    directions = [(1,0), (0,1), (1,1), (1,-1)]

    count = 0

    def backtrack(start_idx: int, placed: int):
        nonlocal count
        # 퀸 n개 놓았으면 해 하나 추가
        if placed == n:
            count += 1
            return

        # 남은 칸은 선형 인덱스 start_idx 이후만 탐색 → 중복 제거
        for idx in range(start_idx, n*n):
            r, c = divmod(idx, n)
            # 구멍(0), 이미 배치된 퀸(1), 또는 공격 표시(>1)이면 건너뛰기
            if board[r][c] is not None:
                continue

            # 3) (r,c)에 퀸 놓기
            board[r][c] = 1
            mark_val = placed + 2  # 공격 표시값
            marked: List[Tuple[int,int]] = []

            # 4) 4방향으로 구멍 전까지 빈 칸(None)을 mark_val로 표시
            for dr, dc in directions:
                rr, cc = r, c
                while True:
                    rr += dr; cc += dc
                    if not (0 <= rr < n and 0 <= cc < n):
                        break
                    if board[rr][cc] == 0:
                        # 구멍 만나면 이 방향 더 이상 표시 금지
                        break
                    if board[rr][cc] is None:
                        board[rr][cc] = mark_val
                        marked.append((rr, cc))

            # 5) 다음 퀸 놓으러 (idx+1부터)
            backtrack(idx + 1, placed + 1)

            # 6) 되돌리기: 공격 표시 해제·퀸 제거
            for rr, cc in marked:
                board[rr][cc] = None
            board[r][c] = None

    # 시작
    backtrack(0, 0)
    return count