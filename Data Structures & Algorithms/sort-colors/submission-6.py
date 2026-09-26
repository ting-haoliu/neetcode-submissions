class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting Sort
        # T: O(n)
        # S: O(1)
        count = [0] * 3
        for num in nums:
            count[num] += 1

        index = 0
        for color in range(len(count)):
            while count[color]:
                nums[index] = color
                count[color] -= 1
                index += 1
