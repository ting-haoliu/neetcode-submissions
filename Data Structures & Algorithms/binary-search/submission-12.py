class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search
        # T: O(log n)
        # S: O(1)
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                return mid
        return -1
        