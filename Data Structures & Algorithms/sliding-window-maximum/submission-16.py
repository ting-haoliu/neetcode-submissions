class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Sliding Window
        # Monotonic Deque
        # T: O(n)
        # S: O(k)
        window = deque()
        res = []

        for i, val in enumerate(nums):
            # 1. Remove indices that are out of the window
            if window and window[0] <= i - k:
                window.popleft()

            # 2. Keep the window sorted in descending order
            while window and val >= nums[window[-1]]:
                window.pop()
            
            # Add the current index
            window.append(i)

            # Append the current max to res
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
