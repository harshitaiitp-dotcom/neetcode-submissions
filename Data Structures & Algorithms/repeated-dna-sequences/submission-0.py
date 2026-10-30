class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        
        # Slide a window of length 10 across the string
        for i in range(len(s) - 9):
            substring = s[i:i+10]
            if substring in seen:
                res.add(substring)
            else:
                seen.add(substring)
                
        return list(res)