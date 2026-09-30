class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch national flag
        # Three Pointers
        # T: O(n)
        # S: O(1)
        
        # [0, L] → 全是 0
        # [L, mid] → 全是 1
        # [R, n-1] → 全是 2
        # [mid, R] → 還沒檢查的區域
        
        # L => 下一個要放0的位置
        # R => 下一個要放2的位置
        # mid => 目前檢查位置
        L, mid, R = 0, 0, len(nums) - 1

        while mid <= R:
            if nums[mid] == 0:
                nums[L], nums[mid] = nums[mid], nums[L]
                L += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[R] = nums[R], nums[mid]
                R -= 1 # mid 不 +1, 因為右邊還沒檢查過
            else:
                mid += 1
