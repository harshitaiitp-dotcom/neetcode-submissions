from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        magazine_counts = Counter(magazine)
        for char in ransomNote:
            if magazine_counts[char] <= 0:
                return False
            magazine_counts[char] -= 1
        return True