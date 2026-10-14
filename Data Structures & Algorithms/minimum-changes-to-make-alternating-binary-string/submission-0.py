class Solution:
    def minOperations(self, s: str) -> int:
        count_start_0 = 0  # Count changes needed for pattern starting with '0'
        
        for i in range(len(s)):
            # Determine expected character based on index
            expected_char = '0' if i % 2 == 0 else '1'
            if s[i] != expected_char:
                count_start_0 += 1
                
        # The changes needed for the pattern starting with '1' 
        # is simply the total length minus the changes for the '0' pattern.
        count_start_1 = len(s) - count_start_0
        
        return min(count_start_0, count_start_1)