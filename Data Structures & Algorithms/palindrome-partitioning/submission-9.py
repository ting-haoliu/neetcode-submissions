class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Backtracking
        # T: O(n * 2^n-1) => a_a_a_a
        # S: O(n)
        res = []

        def backtrack(start: int, path: List[str]) -> None:
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start : end]

                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res
        