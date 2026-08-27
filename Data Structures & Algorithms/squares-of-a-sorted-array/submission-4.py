from collections import deque

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Queue
        # T: O(n)
        # S: O(1)
        L, R = 0, len(nums) - 1
        res = deque()

        while L <= R:
            L_square = nums[L] ** 2
            R_square = nums[R] ** 2

            if abs(nums[L]) < abs(nums[R]):
                res.appendleft(R_square)
                R -= 1
            else:
                res.appendleft(L_square)
                L += 1
        return list(res)
        