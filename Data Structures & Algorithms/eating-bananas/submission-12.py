class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary Search
        # First True
        # T: O(n log m) => m: max(piles)
        # S: O(1)
        L, R = 1, max(piles)

        while L < R:
            mid = (L + R) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)

            if time <= h:
                R = mid
            else:
                L = mid + 1

        return L
        