class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary Search
        # T: O(log x)
        # S: O(1)
        # Last True
        # k^2 <= x => Find the last number that satisfies the condition.
        if x < 2:
            return x

        L, R = 0, x
        while L < R:
            mid = (L + R + 1) // 2

            if mid * mid <= x:
                L = mid
            else:
                R = mid - 1
        return L
              