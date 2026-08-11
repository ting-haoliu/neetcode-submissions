class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS
        # T: O(n * m * 4^L)
        # S: O(L)
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, wordIdx: int) -> bool:
            if wordIdx == len(word):
                return True

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[wordIdx]
            ):
                return False

            tmp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r + 1, c, wordIdx + 1) or
                dfs(r, c + 1, wordIdx + 1) or
                dfs(r - 1, c, wordIdx + 1) or
                dfs(r, c - 1, wordIdx + 1)
            )

            board[r][c] = tmp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
