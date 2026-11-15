from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of each character
        count = Counter(s)
        
        # Sort characters by frequency in descending order
        # If frequencies are the same, python sorts them naturally or we can sort by character
        sorted_chars = sorted(count.keys(), key=lambda x: (-count[x], x))
        
        # Build the resulting string
        return "".join(char * count[char] for char in sorted_chars)