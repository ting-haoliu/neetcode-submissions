class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Greedy
        # T: O(n)
        # S: O(1)
        currMax, maxSum = 0, float('-inf')
        currMin, minSum = 0, float('inf')
        total = 0

        for num in nums:
            currMax = max(num, currMax + num)
            maxSum = max(maxSum, currMax)

            currMin = min(num, currMin + num)
            minSum = min(minSum, currMin)

            total += num

        if maxSum < 0:
            return maxSum

        return max(maxSum, total - minSum)
        