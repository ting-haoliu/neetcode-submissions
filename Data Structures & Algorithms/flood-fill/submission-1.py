class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # DFS
        # T: O(n * m)
        # S: O(n * m)
        startColor = image[sr][sc]
        if startColor == color:
            return image

        rows, cols = len(image), len(image[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r: int, c: int) -> None:
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                image[r][c] != startColor
            ):
                return

            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        dfs(sr, sc)
        return image