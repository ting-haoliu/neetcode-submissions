class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Backtracking
        # T: O(n * 2^n)
        # S: O(n)
        def isPali(word: str) -> bool:
            L, R = 0, len(word) - 1

            while L < R:
                if word[L] != word[R]:
                    return False
                L += 1
                R -= 1
            return True


        res = []

        def backtrack(start: int, path: List[str]) -> None:
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start : end]

                if isPali(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res
