class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Cyclic Sort
        # T: O(n)
        # S: O(1)
        n = len(nums)

        # Put each value in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                correctIdx = nums[i] - 1
                nums[i], nums[correctIdx] = nums[correctIdx], nums[i]

        # Find the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
        