from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Count frequencies of characters in s
        count = Counter(s)
        res = []
        
        # Append characters based on the custom order
        for char in order:
            if char in count:
                res.append(char * count[char])
                del count[char]
                
        # Append any remaining characters not in order
        for char, freq in count.items():
            res.append(char * freq)
            
        return "".join(res)