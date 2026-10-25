class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two Pointers
        # T: O(n^2)
        # S: O(n) => include res
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            L = i + 1
            R = len(nums) - 1
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                
                if total < 0:
                    L += 1
                elif total > 0:
                    R -= 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L - 1] == nums[L]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

        return res
            