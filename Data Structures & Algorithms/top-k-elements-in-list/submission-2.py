class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for n in nums:
            count_map[n] = 1 + count_map.get(n, 0)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, frequency in count_map.items():
            buckets[frequency].append(num)
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result