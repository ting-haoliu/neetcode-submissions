class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Hash Map
        # T: O(n)
        # S: O(n)
        count = {}
        res = []
        n = len(nums)
        threshold = n // 3

        for num in nums:
            count[num] = count.get(num, 0) + 1

            if count[num] == threshold + 1:
                res.append(num)
        
        return res
