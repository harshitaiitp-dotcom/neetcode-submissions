class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # A set to store unique substrings of length k
        code_set = set()
        
        # Total number of unique binary codes of length k is 2^k
        total_codes = 1 << k
        
        # Slide through the string and extract substrings of length k
        for i in range(len(s) - k + 1):
            code_set.add(s[i:i + k])
            # Early exit if we have found all possible codes
            if len(code_set) == total_codes:
                return True
                
        return len(code_set) == total_codes