class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Backtrack
        # T: O(n * n!)
        # S: O(n)
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True

                backtrack(path)

                used[i] = False
                path.pop()
        
        backtrack([])
        return res