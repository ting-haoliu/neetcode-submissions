class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # DFS
        # T: O(n * m)
        # S: O(n * m)
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r: int, c: int, visited: Set) -> int:
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0
            ):
                return 1

            if (r, c) in visited:
                return 0

            visited.add((r, c))

            perimeter = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                perimeter += dfs(nr, nc, visited)
            
            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c, set())
        return 0
