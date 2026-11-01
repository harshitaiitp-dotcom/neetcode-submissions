class Solution:
    def uncommonFromSentences(self, s1: str, s2: str, s3: str = None) -> List[str]:
        # Combine both sentences into a single list of words
        words = s1.split() + s2.split()
        
        # Count the frequency of each word
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
            
        # Return words that appear exactly once overall
        return [word for word in count if count[word] == 1]