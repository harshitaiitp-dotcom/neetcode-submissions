class Solution:
    def minSwaps(self, s: str) -> int:
        extra_closing = 0
        max_extra_closing = 0
        
        for ch in s:
            if ch == '[':
                extra_closing -= 1
            else:
                extra_closing += 1
            
            max_extra_closing = max(max_extra_closing, extra_closing)
            
        return (max_extra_closing + 1) // 2