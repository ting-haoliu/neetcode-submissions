class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window
        # T: O(n)
        # S: O(m)
        res = 0
        count = {}
        maxF = 0

        L = 0
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            maxF = max(maxF, count[s[R]])

            if (R - L + 1) - maxF > k:
                count[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)
        
        return res
        