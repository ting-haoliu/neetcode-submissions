class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS
        # T: O(m * n)
        # S: O(m * n)
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r: int, c: int) -> int:
            queue = deque([(r, c)])
            grid[r][c] = 0
            currArea = 1

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1
                    ):
                        currArea += 1
                        grid[nr][nc] = 0
                        queue.append((nr, nc))
            return currArea

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea