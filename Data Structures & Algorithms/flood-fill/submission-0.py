class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # BFS
        # T: O(n * m)
        # S: O(n * m)
        rows, cols = len(image), len(image[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        startColor = image[sr][sc]
        if startColor == color:
            return image

        queue = deque([(sr, sc)])
        image[sr][sc] = color

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    image[nr][nc] == startColor
                ):
                    image[nr][nc] = color
                    queue.append((nr, nc))

        return image
        