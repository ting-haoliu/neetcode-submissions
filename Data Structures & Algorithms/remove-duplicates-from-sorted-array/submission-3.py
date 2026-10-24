class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Two Pointers
        # T: O(n)
        # S: O(1)
        L = 1

        for R in range(1, len(nums)):
            if nums[R] != nums[L - 1]:
                nums[L] = nums[R]
                L += 1
        return L
        