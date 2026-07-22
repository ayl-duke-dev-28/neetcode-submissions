class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dh, dv in direc:
                nr = r + dh
                nc = c + dv

                if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)
        
        for c in range(cols):
            dfs(0, c, pac)
        for r in range(rows):
            dfs(r, 0, pac)

        for c in range(cols):
            dfs(rows - 1, c, atl)
        for r in range(rows):
            dfs(r, cols - 1, atl)

        ans = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    ans.append([r, c])
        
        return ans