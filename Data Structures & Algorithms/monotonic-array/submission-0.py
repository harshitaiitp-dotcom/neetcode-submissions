class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing = True
        is_decreasing = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                is_increasing = False
            if nums[i] < nums[i + 1]:
                is_decreasing = False
            if not is_increasing and not is_decreasing:
                return False
        return is_increasing or is_decreasing