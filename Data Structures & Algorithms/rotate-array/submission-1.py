class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Reverse algorithm
        # T: O(n)
        # S: O(1)
        # Tip: move the last k elements to the front
        n = len(nums)
        k %= n # rotating n steps results in the same array

        def reverse(L: int, R: int) -> None:
            while L < R:
                nums[L], nums[R] = nums[R], nums[L]

                L += 1
                R -= 1

        # Reverse the entire array
        reverse(0, n - 1)

        # Reverse the first k elements to restore their order
        reverse(0, k - 1)

        # Reverse the remaining elements to restore their order
        reverse(k, n - 1)
        