class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        # T: O(n)
        # S: O(n)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res
        return []
