class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary Search
        # T: O(log n)
        # S: O(1)
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        # the element on the L position is the first one
        # > or = target
        return L
        