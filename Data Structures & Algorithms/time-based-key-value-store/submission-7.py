class TimeMap:
    # Binary Search
    # S: O(n)
    def __init__(self):
        # {key1: [(timestamp1, value1), (timestamp2, value2)]}
        self.store = defaultdict(list)

    # T: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    # T: O(log n)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]

        if values[0][0] > timestamp:
            return ""

        L, R = 0, len(values) - 1

        while L < R:
            # Last True
            mid = (L + R + 1) // 2

            if values[mid][0] <= timestamp:
                L = mid
            else:
                R = mid - 1
        return values[R][1]
