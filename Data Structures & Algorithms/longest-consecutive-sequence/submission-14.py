class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hash Set
        # T: O(n)
        # S: O(n)
        numSet = set(nums) # O(n)
        res = 0

        for num in numSet:
            if (num - 1) not in numSet:
                currNum = num
                length = 1

                while (currNum + 1) in numSet:
                    currNum += 1
                    length += 1
                
                res = max(res, length)
        
        return res
        