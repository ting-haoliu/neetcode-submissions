class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # DFS
        # T: O(n * m)
        # S: O(n * m)
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r: int, c: int) -> None:
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != 'O'
            ):
                return

            board[r][c] = '#'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                dfs(nr, nc)

        # Replace 'O' to '#' on the edges
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'
