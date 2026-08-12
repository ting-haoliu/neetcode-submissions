class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        # T: O(m * n)
        # S: O(m * n)
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r: int, c: int) -> None:
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == '0'
            ):
                return

            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands