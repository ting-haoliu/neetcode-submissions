class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Backtrack
        # Sorting
        # T: O(n * 2^n)
        # S: O(n)
        nums.sort()
        res = []

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                # skip duplicates at the same depth
                if i > start and nums[i - 1] == nums[i]:
                    continue
                
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
        