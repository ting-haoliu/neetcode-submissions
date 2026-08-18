class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Iteration
        # T: O(n * m)
        # S: O(1)
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4

                    # cell from top
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
                    
                    # cell from left
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
        return perimeter
