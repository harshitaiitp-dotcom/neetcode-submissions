class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Find the maximum frequency required for each letter across all strings in words2
        max_freq = [0] * 26
        for word in words2:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            for i in range(26):
                max_freq[i] = max(max_freq[i], freq[i])
        
        # Filter words1 based on the maximum frequency requirements
        result = []
        for word in words1:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            
            valid = True
            for i in range(26):
                if freq[i] < max_freq[i]:
                    valid = False
                    break
            if valid:
                result.append(word)
                
        return result