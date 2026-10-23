from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count the frequency of each character in the string
        count = Counter(s)
        
        # Iterate through the string with indices to find the first character with a count of 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
                
        # Return -1 if no unique character exists
        return -1