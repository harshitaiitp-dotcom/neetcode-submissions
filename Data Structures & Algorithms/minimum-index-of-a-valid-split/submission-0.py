class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the dominant element and its total count in the array
        total_count = {}
        for num in nums:
            total_count[num] = total_count.get(num, 0) + 1
            
        dominant = -1
        total_freq = 0
        n = len(nums)
        
        for num, freq in total_count.items():
            if freq * 2 > n:
                dominant = num
                total_freq = freq
                break
                
        # Step 2: Iterate through possible split indices and check conditions
        left_freq = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                left_freq += 1
                
            right_freq = total_freq - left_freq
            
            # Check if dominant in both left and right subarrays
            if left_freq * 2 > (i + 1) and right_freq * 2 > (n - 1 - i):
                return i
                
        return -1