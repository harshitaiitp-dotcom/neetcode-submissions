from collections import Counter
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq = Counter(arr)
        lucky = [num for num, count in freq.items() if num == count]
        return max(lucky) if lucky else -1