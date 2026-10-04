class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Hash Map
        # T: O(n)
        # S: O(n)
        count = {}
        res = set()
        n = len(nums)

        for num in nums:
            count[num] = count.get(num, 0) + 1

            if count[num] > (n / 3):
                res.add(num)
        
        return list(res)
