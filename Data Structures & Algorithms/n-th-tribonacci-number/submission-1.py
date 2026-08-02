class Solution:
    def tribonacci(self, n: int) -> int:
        # T: O(n)
        # S: O(1)
        if n < 1:
            return n
        
        if n == 2:
            return 1

        curr = 0
        prev3, prev2, prev1 = 0, 1, 1
        for _ in range(3, n + 1):
            curr = prev3 + prev2 + prev1
            prev3 = prev2
            prev2 = prev1
            prev1 = curr

        return prev1