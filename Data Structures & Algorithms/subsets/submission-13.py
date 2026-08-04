class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking
        # T: O(n * 2^n) => n, copy of path
        # S: O(n)
        '''
        []
        ├── [1]
        │   ├── [1, 2]
        │   │   └── [1, 2, 3]
        │   └── [1, 3]
        ├── [2]
        │   └── [2, 3]
        └── [3]
        '''
        res = []

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i]) # choose
                backtrack(i + 1, path) # explore
                path.pop() # undo

        backtrack(0, [])
        return res
