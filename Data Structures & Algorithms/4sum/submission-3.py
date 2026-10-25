class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Two Pointers
        # T: O(n^3)
        # S: O(1)
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n - 3):
            # skip
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            if (nums[i] + nums[i + 1] +
                nums[i + 2] + nums[i + 3]) > target:
                break
            if (nums[i] + nums[n - 3] +
                nums[n - 2] + nums[n - 1]) < target:
                continue
            
            for j in range(i + 1, n - 2):
                #skip
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                if (nums[i] + nums[j] +
                    nums[j + 1] + nums[j + 2]) > target:
                    break
                if (nums[i] + nums[j] +
                    nums[n - 2] + nums[n - 1]) < target:
                    continue

                L, R = j + 1, n - 1
                while L < R:
                    total = nums[i] + nums[j] + nums[L] + nums[R]

                    if total < target:
                        L += 1
                    elif total > target:
                        R -= 1
                    else:
                        res.append([nums[i], nums[j],
                                nums[L], nums[R]])
                        L += 1
                        R -= 1

                        while L < R and nums[L - 1] == nums[L]:
                            L += 1
                        while L < R and nums[R + 1] == nums[R]:
                            R -= 1
        return res
