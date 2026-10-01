class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Min Heap
        # T: O(n log k)
        # S: O(n + k)
        count = {}
        for num in nums: # O(n)
            count[num] = count.get(num, 0) + 1

        min_heap = []
        for num, freq in count.items(): # O(n log k)
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        for i in range(len(min_heap)): # O(k log k)
            res.append(heapq.heappop(min_heap)[1])

        return res
        