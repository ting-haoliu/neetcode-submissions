class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking
        # T: O(Cₙ)
        # S: O(n) => O(2n)
        res = []

        def backtrack(L: int, R: int, path: List[str]) -> None:
            if len(path) == n * 2:
                res.append("".join(path))
                return

            if L < n:
                path.append("(")
                backtrack(L + 1, R, path)
                path.pop()

            if R < L:
                path.append(")")
                backtrack(L, R + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return res