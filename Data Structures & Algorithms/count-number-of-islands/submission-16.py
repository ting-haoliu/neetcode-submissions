class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        # T: O(m * n)
        # S: O(m * n)
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            grid[r][c] = '0'

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == '1'
                    ):
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        return islands
