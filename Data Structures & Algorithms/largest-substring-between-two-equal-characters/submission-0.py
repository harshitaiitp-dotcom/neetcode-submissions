class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occurrence = {}
        max_len = -1
        
        for i, char in enumerate(s):
            if char in first_occurrence:
                # Calculate the length of the substring between the first and current occurrence
                max_len = max(max_len, i - first_occurrence[char] - 1)
            else:
                # Store the first seen index of the character
                first_occurrence[char] = i
                
        return max_len