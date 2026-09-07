from collections import defaultdict
from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        good_pairs = 0      
        for num in nums:
            good_pairs += count[num]
            count[num] += 1
        return good_pairs