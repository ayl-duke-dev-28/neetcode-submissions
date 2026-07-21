from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        
        while queue:
            r, c, minute = queue.popleft()
            for row_step, col_step in directions:
                next_row = r + row_step
                next_col = c + col_step
                if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 1:
                    grid[next_row][next_col] = 2
                    fresh -= 1
                    minutes = minute + 1
                    queue.append((next_row, next_col, minute + 1))

        return minutes if fresh == 0 else -1