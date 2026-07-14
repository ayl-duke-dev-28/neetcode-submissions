from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        inf = 2147483647
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
        
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, dist = queue.popleft()

            for row_step, col_step in direc:
                next_row = r + row_step
                next_col = c + col_step
                if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == inf:
                    grid[next_row][next_col] = dist + 1
                    queue.append((next_row, next_col, dist + 1))