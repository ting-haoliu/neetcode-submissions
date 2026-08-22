class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS
        # T: O(n^2)
        # S: O(n^2)
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = deque([(0, 0, 1)]) # r, c, length
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, -1), (-1, 1)
        ]

        while queue:
            r, c, length = queue.popleft()

            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < n and
                    0 <= nc < n and
                    grid[nr][nc] == 0
                ):
                    queue.append((nr, nc, length + 1))
                    grid[nr][nc] = 1
        
        return -1
