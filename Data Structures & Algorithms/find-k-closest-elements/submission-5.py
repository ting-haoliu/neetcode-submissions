class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary Search
        # T: O(log(n - k))
        # S: O(1)
        if len(arr) == k:
            return arr

        L, R = 0, len(arr) - k # Find the left starting point

        while L < R:
            mid = (L + R) // 2

            # arr[mid] => the left most element in current window
            # arr[mid + k] => the new elements will be added if the window move right
            if x - arr[mid] > arr[mid + k] - x:
                L = mid + 1
            else:
                R = mid
        return arr[L : L + k]
