class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * len(nums)
        self.prefix[0] = nums[0]

        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        prefixRight = self.prefix[right]
        prefixLeft = self.prefix[left - 1] if left > 0 else 0

        return prefixRight - prefixLeft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)