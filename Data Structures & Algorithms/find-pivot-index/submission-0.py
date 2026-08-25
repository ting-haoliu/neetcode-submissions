class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Prefix Sum
        # T: O(n)
        # S: O(n)
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        n = len(nums)

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        if prefix[n - 1] - prefix[0] == 0:
            return 0

        for i in range(1, n):
            if prefix[i - 1] == prefix[n - 1] - prefix[i]:
                return i
        return -1
