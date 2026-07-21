class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def backtrack(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return (1 + backtrack(r - 1, c) + backtrack(r + 1, c) + backtrack(r, c - 1) + backtrack(r, c + 1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, backtrack(i, j))

        return max_area 