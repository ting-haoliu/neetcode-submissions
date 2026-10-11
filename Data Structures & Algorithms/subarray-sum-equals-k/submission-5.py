class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix Sum
        # Hash Map
        # T: O(n)
        # S: O(n)
        # SubarraySum(i, j) = Sum(j) − Sum(i−1)
        # prefixSum = Sum(i-1), k = SubarraySum(i, j), currSum = Sum(j)
        # => currSum - k = prefixSum

        prefixSum = {0 : 1} # {sum : freq}
        res = 0
        currSum = 0

        for num in nums:
            currSum += num
            prevSum = currSum - k

            if prevSum in prefixSum:
                res += prefixSum[prevSum]

            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        
        return res
