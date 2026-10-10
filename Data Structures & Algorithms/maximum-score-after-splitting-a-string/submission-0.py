class Solution:
    def maxScore(self, s: str) -> int:
        # Count total ones in the string
        total_ones = s.count('1')
        
        zeros_left = 0
        ones_left = 0
        max_score = 0
        
        # Iterate through all valid split points (excluding the last character)
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_left += 1
            
            # Right ones = Total ones - Ones in the left part
            ones_right = total_ones - ones_left
            
            # Current score = Zeros in left + Ones in right
            current_score = zeros_left + ones_right
            
            max_score = max(max_score, current_score)
            
        return max_score