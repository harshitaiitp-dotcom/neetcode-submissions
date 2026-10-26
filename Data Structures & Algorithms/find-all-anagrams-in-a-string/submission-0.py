from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        
        p_count = Counter(p)
        window_count = Counter(s[:m])
        
        res = []
        if p_count == window_count:
            res.append(0)
            
        for i in range(m, n):
            # Add the new character entering the window on the right
            left_char = s[i - m]
            window_count[s[i]] += 1
            
            # Remove the character leaving the window from the left
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
                
            # Compare counts
            if window_count == p_count:
                res.append(i - m + 1)
                
        return res