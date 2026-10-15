class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        
        # Dictionary or array to store the total count of each character
        char_count = {}
        
        for word in words:
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1
                
        # Check if every character's count is divisible by n
        for char, count in char_count.items():
            if count % n != 0:
                return False
                
        return True