class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # BFS
        # T: O(n * m)
        # S: O(n * m)
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r: int, c: int, visited: Set) -> int:
            queue = deque([(r, c)])
            visited.add((r, c))
            perimeter = 0

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        grid[nr][nc] == 0
                    ):
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c, set())
        return 0