class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Sliding Window
        # Hash Set
        # T: O(n)
        # S: O(k)
        seen = set()

        L = 0
        for R in range(len(nums)):
            if (R - L) > k:
                seen.remove(nums[L])
                L += 1

            if nums[R] in seen:
                return True
            
            seen.add(nums[R])
        return False
        