class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Combinations
        # Hash Map
        # T: O(n * 4^n)
        # S: O(n)
        if not digits:
            return []

        digitMap = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        res = []
        def backtrack(i: int, path: List[str]) -> None:
            if len(path) == len(digits):
                res.append("".join(path))
                return

            digit = digits[i]
            for c in digitMap[digit]:
                path.append(c)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
        