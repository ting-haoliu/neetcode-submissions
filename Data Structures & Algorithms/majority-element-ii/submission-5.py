class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore Voting
        # T: O(n)
        # S: O(1)

        # At most two candidates greater than n/3
        cand1, cand2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        threshold = len(nums) / 3

        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > threshold:
                res.append(cand)
        return res
