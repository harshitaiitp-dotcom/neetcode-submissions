class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for x in range(1, n + 1):
            if nums[x - 1] >= x:
                if x == n or nums[x] < x:
                    return x    
        return -1