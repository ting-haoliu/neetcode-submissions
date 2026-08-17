class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS
        # T: O(n * m)
        # S: O(n * m)
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(
            r: int, c: int, visited: Set, prevH: int
        ) -> None:
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                prevH > heights[r][c]
            ):
                return

            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                dfs(nr, nc, visited, heights[r][c])

        # Put cells in visited
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (
                    (r, c) in pac and
                    (r, c) in atl
                ):
                    res.append([r, c])
        return res