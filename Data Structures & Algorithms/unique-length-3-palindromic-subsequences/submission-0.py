class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}
        
        # Record the first and last occurrence of each character
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        ans = 0
        
        # Check for each unique character from 'a' to 'z'
        for char in first:
            if last[char] - first[char] > 1:
                # Find unique characters between the first and last occurrence
                unique_middle_chars = set(s[first[char] + 1 : last[char]])
                ans += len(unique_middle_chars)
                
        return ans