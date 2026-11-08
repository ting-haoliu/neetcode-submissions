class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary Search
        # T: O(log n)
        # S: O(1)
        L, R = 0, len(nums) - 1

        while L < R:
            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        
        return nums[L]
        