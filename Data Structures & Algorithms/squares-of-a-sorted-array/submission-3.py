class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # T: O(n)
        # S: O(1)
        n = len(nums)
        res = [0] * n
        L, R = 0, n - 1
        index = n - 1

        while L <= R:
            if abs(nums[L]) < abs(nums[R]):
                res[index] = nums[R] ** 2
                R -= 1
            else:
                res[index] = nums[L] ** 2
                L += 1
            index -= 1
        return res
