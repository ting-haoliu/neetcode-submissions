class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Binary Search
        # T: O(log n)
        # S: O(1)
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] == target:
                return True

            if nums[mid] > nums[R]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            elif nums[mid] < nums[R]:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
            # nums[mid] == nums[R] => Cannot determine which half is sorted
            else:
                R -= 1
        return False
