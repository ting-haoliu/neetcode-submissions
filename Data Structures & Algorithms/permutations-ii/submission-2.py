class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Backtrack
        # Sort
        # T: O(n * n!)
        # S: O(n)
        res = []
        used = [False] * (len(nums))
        nums.sort()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if (i > 0 and nums[i - 1] == nums[i] and
                    not used[i - 1]):
                    continue
                
                path.append(nums[i])
                used[i] = True

                backtrack(path)

                path.pop()
                used[i] = False
            
        backtrack([])
        return res