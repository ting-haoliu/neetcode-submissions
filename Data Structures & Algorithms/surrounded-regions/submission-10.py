class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # BFS
        # T: O(n * m)
        # S: O(n * m)
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = deque()
        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == 'O':
                    queue.append((r, c))
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == 'O':
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            board[r][c] = '#'
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] == 'O'
                ):
                    queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'