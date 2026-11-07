class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Binary Search
        # T: O(n log(sum(weights) - max(weights)))
        # S: O(1)
        L, R = max(weights), sum(weights)

        def can_ship(capacity: int) -> bool:
            need_days = 1
            curr_load = 0

            for w in weights:
                if curr_load + w > capacity:
                    need_days += 1
                    curr_load = 0
                curr_load += w

            return need_days <= days

        while L < R:
            mid = (L + R) // 2

            if can_ship(mid):
                R = mid
            else:
                L = mid + 1
        return L